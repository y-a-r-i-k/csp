import tkinter as tk
from tkinter import ttk, messagebox

class SalaryCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор зарплаты преподавателя")
        
        # Создаем главное меню
        self.create_main_menu()
        
        # Создаем вкладки
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10, fill='both', expand=True)
        
        self.create_salary_tab()
        
        # Переключатель для налога
        self.tax_var = tk.BooleanVar(value=True)
        self.tax_check = tk.Checkbutton(
            root, text="Учесть единый налог (13%)", 
            variable=self.tax_var, 
            command=self.toggle_tax
        )
        self.tax_check.pack(pady=5)
        
        # Кнопка расчета
        self.calc_button = tk.Button(
            root, text="Рассчитать зарплату", 
            command=self.calculate_salary,
            state=tk.NORMAL
        )
        self.calc_button.pack(pady=10)
        
        # Поле для вывода результата
        self.result_label = tk.Label(root, text="", font=('Arial', 12))
        self.result_label.pack(pady=10)
    
    def create_main_menu(self):
        menubar = tk.Menu(self.root)
        
        # Главное меню
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Выход", command=self.root.quit)
        menubar.add_cascade(label="Файл", menu=file_menu)
        
        # Контекстное меню
        self.context_menu = tk.Menu(menubar, tearoff=0)
        self.context_menu.add_command(label="Очистить", command=self.clear_fields)
        
        self.root.bind("<Button-3>", self.show_context_menu)
        
        self.root.config(menu=menubar)
    
    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)
    
    def create_salary_tab(self):
        tab1 = ttk.Frame(self.notebook)
        self.notebook.add(tab1, text="Зарплата")
        
        # Поле для ввода количества часов
        tk.Label(tab1, text="Количество часов:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.hours_entry = tk.Entry(tab1)
        self.hours_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Переключатель для должности
        tk.Label(tab1, text="Должность:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        
        self.position_var = tk.StringVar(value="assistant")
        positions = [
            ("Ассистент (275 руб/час)", "assistant"),
            ("Доцент (450 руб/час)", "docent"),
            ("Профессор (650 руб/час)", "professor")
        ]
        
        for i, (text, value) in enumerate(positions):
            rb = tk.Radiobutton(
                tab1, text=text, 
                variable=self.position_var, 
                value=value
            )
            rb.grid(row=i+2, column=0, columnspan=2, padx=5, pady=2, sticky='w')
    
    def toggle_tax(self):
        pass
    
    def clear_fields(self):
        self.hours_entry.delete(0, tk.END)
        self.position_var.set("assistant")
        self.result_label.config(text="")
    
    def calculate_salary(self):
        try:
            hours = float(self.hours_entry.get())
            if hours <= 0:
                raise ValueError("Количество часов должно быть положительным числом")
            
            position = self.position_var.get()
            rates = {
                "assistant": 275,
                "docent": 450,
                "professor": 650
            }
            rate = rates[position]
            
            salary = hours * rate
            
            if self.tax_var.get():
                salary *= 0.87  # Учет налога 13%
            
            position_names = {
                "assistant": "Ассистент",
                "docent": "Доцент",
                "professor": "Профессор"
            }
            
            result_text = (
                f"{position_names[position]}, {hours} часов\n"
                f"Зарплата: {salary:.2f} руб."
            )
            self.result_label.config(text=result_text)
            
        except ValueError as e: #Выброс ошибки
            messagebox.showerror("Ошибка", str(e))
    

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryCalculatorApp(root)
    root.mainloop()