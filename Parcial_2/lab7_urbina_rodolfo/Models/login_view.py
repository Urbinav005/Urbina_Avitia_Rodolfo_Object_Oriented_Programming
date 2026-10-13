import tkinter as tk
from tkinter import messagebox
from Models.login_model import user
from Views.home_view import DashBoardventana

class login_window():
    def __init__(self, root):
        self.root = root
        self.root.title("inicio de sesion al sistema")
        self.root.geometr("300x300")
        self.root.resizable(False, False)
