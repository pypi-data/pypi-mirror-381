import sys
import os
from typing import Dict, List

try:
    import customtkinter as ctk
except Exception as exc:  # pragma: no cover
    raise SystemExit("customtkinter is required: pip install customtkinter") from exc

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    _HAS_DND = True
except Exception:
    # Drag-and-drop is optional; we'll gracefully fall back to a file dialog
    from tkinter import Tk as _Tk
    _HAS_DND = False

import tkinter as tk
from tkinter import filedialog, messagebox

from .management.commands.generate_model import DjangoMGGenerator


class ScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master: tk.Misc, options: Dict[str, Dict]):
        super().__init__(master)
        self.code_to_var: Dict[str, tk.BooleanVar] = {}
        # Show in numeric order
        for code in sorted(options.keys(), key=lambda x: int(x)):
            config = options[code]
            label_text = f"{code} - {config['help']}"
            var = tk.BooleanVar(value=False)
            cb = ctk.CTkCheckBox(self, text=label_text, variable=var)
            cb.pack(anchor="w", pady=2, padx=4)
            self.code_to_var[code] = var

    def get_selected_codes(self) -> List[str]:
        selected = [code for code, var in self.code_to_var.items() if var.get()]
        return sorted(selected, key=lambda x: int(x))

    def select_all(self) -> None:
        for var in self.code_to_var.values():
            var.set(True)

    def clear_all(self) -> None:
        for var in self.code_to_var.values():
            var.set(False)


class App:
    def __init__(self) -> None:
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Root: prefer TkinterDnD for native drop support if available
        if _HAS_DND:
            self.root = TkinterDnD.Tk()
        else:
            self.root = _Tk()

        self.root.title("Django-MG - Model Generator (GUI)")
        self.root.geometry("980x720")

        # State
        self.selected_file: str = ""
        self.category_frames: Dict[str, ScrollableCheckboxFrame] = {}

        # Layout
        self._build_layout()

    def _build_layout(self) -> None:
        # Header
        header = ctk.CTkFrame(self.root)
        header.pack(fill="x", padx=12, pady=(12, 8))
        ctk.CTkLabel(
            header,
            text="Django-MG | تولید مدل جنگو",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(side="left", padx=8)

        # File selector + class + fields
        top_frame = ctk.CTkFrame(self.root)
        top_frame.pack(fill="x", padx=12, pady=12)

        # File selector area
        self.file_label = ctk.CTkLabel(top_frame, text="فایل models.py رو اینجا درگ کنید یا انتخاب کنید")
        self.file_label.pack(anchor="w", padx=8, pady=8)

        drop_frame = ctk.CTkFrame(top_frame, height=80)
        drop_frame.pack(fill="x", padx=8, pady=(0, 8))
        drop_frame.pack_propagate(False)

        self.drop_area = ctk.CTkLabel(drop_frame, text="Drag & Drop here", fg_color=("#2b2b2b", "#e8e8e8"))
        self.drop_area.pack(fill="both", expand=True, padx=8, pady=8)

        if _HAS_DND:
            # Register drop target
            self.drop_area.drop_target_register(DND_FILES)
            self.drop_area.dnd_bind("<<Drop>>", self._on_file_drop)

        browse_btn = ctk.CTkButton(top_frame, text="انتخاب فایل...", command=self._browse_file)
        browse_btn.pack(anchor="w", padx=8, pady=(0, 8))

        # Class name input
        form_frame = ctk.CTkFrame(self.root)
        form_frame.pack(fill="x", padx=12, pady=(0, 12))

        ctk.CTkLabel(form_frame, text="نام کلاس (ClassName)").pack(anchor="w", padx=8, pady=(8, 4))
        self.class_entry = ctk.CTkEntry(form_frame, placeholder_text="مثلاً: Product")
        self.class_entry.pack(fill="x", padx=8, pady=(0, 8))

        # Middle section: fields + requirements side-by-side
        mid_container = ctk.CTkFrame(self.root)
        mid_container.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        # Left: Checkbox list of fields (categorized tabs)
        left_panel = ctk.CTkFrame(mid_container)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 6), pady=0)

        ctk.CTkLabel(left_panel, text="فیلدها را انتخاب کنید:").pack(anchor="w", padx=8, pady=(8, 4))

        self.tabs = ctk.CTkTabview(left_panel)
        self.tabs.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self._build_field_tabs()

        # Right: Requirements box (copyable)
        right_panel = ctk.CTkFrame(mid_container, width=340)
        right_panel.pack(side="right", fill="y", padx=(6, 0))
        right_panel.pack_propagate(False)

        ctk.CTkLabel(right_panel, text="بسته‌های مورد نیاز (قابل کپی)").pack(anchor="w", padx=8, pady=(8, 4))
        self.pip_box = ctk.CTkTextbox(right_panel, height=180)
        self.pip_box.pack(fill="x", padx=8, pady=(0, 6))
        self.pip_box.insert("1.0", "پس از انتخاب فیلدها و تولید، دستورات مورد نیاز اینجا نمایش داده می‌شود")
        self.pip_box.configure(state="disabled")

        self.copy_btn = ctk.CTkButton(right_panel, text="کپی دستورات", command=self._copy_requirements, state="disabled")
        self.copy_btn.pack(anchor="e", padx=8, pady=(0, 12))

        # Actions
        actions = ctk.CTkFrame(self.root)
        actions.pack(fill="x", padx=12, pady=(0, 12))

        left = ctk.CTkFrame(actions)
        left.pack(side="left", padx=8)

        ctk.CTkButton(left, text="انتخاب همه در تب", command=self._select_all_in_tab).pack(side="left", padx=4)
        ctk.CTkButton(left, text="پاک کردن تب", command=self._clear_tab).pack(side="left", padx=4)
        ctk.CTkButton(left, text="انتخاب همه", command=self._select_all_global).pack(side="left", padx=4)
        ctk.CTkButton(left, text="پاک کردن همه", command=self._clear_all_global).pack(side="left", padx=4)

        ctk.CTkButton(actions, text="تولید مدل", command=self._on_generate).pack(side="right", padx=8)

        # Footer
        self.status = ctk.CTkLabel(self.root, text="آماده")
        self.status.pack(fill="x", padx=12, pady=(0, 12))

    def _build_field_tabs(self) -> None:
        # Categories mapped to codes (based on README guide)
        cat_map: Dict[str, List[str]] = {
            "عمومی": ["01","02","07","08","84","85","86","87"],
            "رسانه": ["34","35","36","37","38","39","88","89"],
            "فروشگاهی": ["14","15","16","66","67","68","64","65"],
            "روابط": ["51","52","53","54","55","56","57"],
            "زمان": ["17","18","19","20","90","99"],
            "پرچم‌ها": ["24","25","96"],
            "SEO / Meta": ["03","26","79","80"],
            "تماس": ["28","29","30","31"],
            "مکان": ["32","61","75","62","63"],
            "GIS": ["58","59","60"],
            "امنیت": ["49","50","71"],
            "پیشرفته": ["44","45","46","47","48","70","83"],
            "تاریخ/نسخه": ["76","77","78"],
            "بین‌الملل": ["74","93"],
            "UI": ["69"],
            "Postgres": ["81","82"],
        }
        all_config = DjangoMGGenerator.FIELDS_CONFIG
        for cat, codes in cat_map.items():
            tab = self.tabs.add(cat)
            # Build filtered options dict for this category
            options = {code: all_config[code] for code in codes if code in all_config}
            frame = ScrollableCheckboxFrame(tab, options)
            frame.pack(fill="both", expand=True, padx=6, pady=6)
            self.category_frames[cat] = frame

    def _set_status(self, text: str) -> None:
        self.status.configure(text=text)

    def _on_file_drop(self, event) -> None:
        # event.data can contain braces and multiple paths
        data = event.data.strip()
        if data.startswith("{") and data.endswith("}"):
            data = data[1:-1]
        # Split by whitespace, take first
        path = data.split()[:1][0]
        self._set_selected_file(path)

    def _browse_file(self) -> None:
        file_path = filedialog.askopenfilename(
            title="Select models.py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")],
        )
        if file_path:
            self._set_selected_file(file_path)

    def _set_selected_file(self, path: str) -> None:
        self.selected_file = path
        self.drop_area.configure(text=os.path.abspath(path))
        self._set_status(f"فایل انتخاب شد: {os.path.basename(path)}")

    def _collect_selected_codes(self) -> List[str]:
        selected: List[str] = []
        for frame in self.category_frames.values():
            selected.extend(frame.get_selected_codes())
        # Deduplicate and sort
        return sorted(list(set(selected)), key=lambda x: int(x))

    def _select_all_in_tab(self) -> None:
        active = self.tabs.get()
        if active in self.category_frames:
            self.category_frames[active].select_all()

    def _clear_tab(self) -> None:
        active = self.tabs.get()
        if active in self.category_frames:
            self.category_frames[active].clear_all()

    def _select_all_global(self) -> None:
        for frame in self.category_frames.values():
            frame.select_all()

    def _clear_all_global(self) -> None:
        for frame in self.category_frames.values():
            frame.clear_all()

    def _on_generate(self) -> None:
        if not self.selected_file:
            messagebox.showerror("خطا", "ابتدا یک فایل مقصد (مثلاً models.py) انتخاب یا دراپ کنید")
            return

        class_name = (self.class_entry.get() or "").strip()
        if not class_name:
            messagebox.showerror("خطا", "نام کلاس را وارد کنید")
            return

        # Validate class name: simple CamelCase suggestion
        if not class_name[0].isalpha():
            messagebox.showerror("خطا", "نام کلاس باید با حرف شروع شود")
            return

        codes = self._collect_selected_codes()
        field_numbers = "/".join(codes)

        # Ensure file endswith .py; generator handles adding if missing, but here we pass exact file
        file_name = self.selected_file

        try:
            self._set_status("در حال تولید مدل...")
            result_msg, pip_cmds = DjangoMGGenerator.generate_model(file_name=file_name, class_name=class_name, field_numbers=field_numbers)
        except Exception as exc:
            self._set_status("خطا")
            messagebox.showerror("خطا", str(exc))
            return

        self._set_status("انجام شد")

        # Show result info
        messagebox.showinfo("نتیجه", result_msg)

        # Populate requirements box
        if pip_cmds:
            unique_pip = sorted(set(pip_cmds))
            pip_line = "pip install " + " ".join(unique_pip)
            self._set_requirements_text(pip_line)
        else:
            self._set_requirements_text("نیازی به نصب بسته اضافی نیست")

    def _set_requirements_text(self, text: str) -> None:
        self.pip_box.configure(state="normal")
        self.pip_box.delete("1.0", tk.END)
        self.pip_box.insert("1.0", text)
        self.pip_box.configure(state="disabled")
        self.copy_btn.configure(state="normal" if text.strip() else "disabled")

    def _copy_requirements(self) -> None:
        try:
            self.root.clipboard_clear()
            content = self.pip_box.get("1.0", tk.END).strip()
            if content:
                self.root.clipboard_append(content)
                self._set_status("دستورات کپی شد")
        except Exception:
            pass

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()


