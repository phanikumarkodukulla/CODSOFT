import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.filename = "tasks.json"
        self.tasks = self.load_tasks()
        self.setup_gui()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("My Todo List")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        title_label = tk.Label(main_frame, text="Todo List Manager", 
                              font=('Arial', 16, 'bold'), bg='#f0f0f0')
        title_label.pack(pady=(0, 10))
        
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(input_frame, text="New Task:", bg='#f0f0f0').pack(side=tk.LEFT)
        self.task_entry = tk.Entry(input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=(5, 5))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        add_btn = tk.Button(input_frame, text="Add Task", command=self.add_task,
                           bg='#4CAF50', fg='white', relief=tk.FLAT)
        add_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        list_frame = tk.Frame(main_frame, bg='#f0f0f0')
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                      font=('Arial', 10), selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        complete_btn = tk.Button(button_frame, text="Mark Complete", 
                               command=self.mark_complete, bg='#2196F3', 
                               fg='white', relief=tk.FLAT)
        complete_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        delete_btn = tk.Button(button_frame, text="Delete Task", 
                             command=self.delete_task, bg='#f44336', 
                             fg='white', relief=tk.FLAT)
        delete_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        clear_btn = tk.Button(button_frame, text="Clear Completed", 
                            command=self.clear_completed, bg='#FF9800', 
                            fg='white', relief=tk.FLAT)
        clear_btn.pack(side=tk.LEFT)
        
        self.refresh_list()
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            new_task = {
                'id': len(self.tasks) + 1,
                'text': task_text,
                'completed': False,
                'created': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
            self.tasks.append(new_task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def mark_complete(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_id = self.get_task_id_from_display(index)
            for task in self.tasks:
                if task['id'] == task_id:
                    task['completed'] = not task['completed']
                    break
            self.save_tasks()
            self.refresh_list()
        else:
            messagebox.showinfo("Info", "Please select a task first!")
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_id = self.get_task_id_from_display(index)
            self.tasks = [t for t in self.tasks if t['id'] != task_id]
            self.save_tasks()
            self.refresh_list()
        else:
            messagebox.showinfo("Info", "Please select a task to delete!")
    
    def clear_completed(self):
        self.tasks = [t for t in self.tasks if not t['completed']]
        self.save_tasks()
        self.refresh_list()
    
    def get_task_id_from_display(self, display_index):
        visible_tasks = [t for t in self.tasks]
        if display_index < len(visible_tasks):
            return visible_tasks[display_index]['id']
        return None
    
    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            display_text = f"{status} {task['text']}"
            if task['completed']:
                display_text = f"{display_text} (Done)"
            self.task_listbox.insert(tk.END, display_text)
    
    def run(self):
        self.root.mainloop()

class CommandLineTodo:
    def __init__(self):
        self.filename = "tasks.json"
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        
        print("\n=== Your Tasks ===")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else "○"
            print(f"{i}. {status} {task['text']}")
        print()
    
    def add_task(self):
        task_text = input("Enter new task: ").strip()
        if task_text:
            new_task = {
                'id': len(self.tasks) + 1,
                'text': task_text,
                'completed': False,
                'created': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
            self.tasks.append(new_task)
            self.save_tasks()
            print(f"Task '{task_text}' added successfully!")
        else:
            print("Task cannot be empty!")
    
    def complete_task(self):
        self.show_tasks()
        try:
            task_num = int(input("Enter task number to mark complete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1]['completed'] = True
                self.save_tasks()
                print("Task marked as complete!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def delete_task(self):
        self.show_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(self.tasks):
                deleted_task = self.tasks.pop(task_num - 1)
                self.save_tasks()
                print(f"Task '{deleted_task['text']}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def run(self):
        while True:
            print("\n=== Todo List Manager ===")
            print("1. View tasks")
            print("2. Add task")
            print("3. Mark task complete")
            print("4. Delete task")
            print("5. Exit")
            
            choice = input("Choose an option (1-5): ").strip()
            
            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    print("Choose interface:")
    print("1. GUI (Graphical)")
    print("2. Command Line")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        app = TodoApp()
        app.run()
    elif choice == '2':
        cli_app = CommandLineTodo()
        cli_app.run()
    else:
        print("Invalid choice! Starting GUI by default...")
        app = TodoApp()
        app.run()