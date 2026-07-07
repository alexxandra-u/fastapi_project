"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random

from rxconfig import config
from .ml_model import predict


def application_form() -> rx.Component:
    """Форма подачи заявки на кредитную карту."""
    return rx.form(
        rx.vstack(
            rx.heading("Fill the form", size="5"),
            
            # Имя
            rx.text("Name", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter your name",
                name="name", 
                required=True,
            ),
            
            # Email
            rx.text("Email", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter your email",
                name="email",
                type="email",
                required=True,
            ),
            
            # Пол
            rx.text("Gender", size="3", font_weight="bold"),
            rx.select(
                ["Male", "Female", "Other"], 
                placeholder="Select gender",
                name="gender",
                required=True,
            ),
            
            # Возраст
            rx.text("Age", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter your age",
                name="age",
                type="number",
            ),

            # День рождения
            rx.text("Date of Birth", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter your date of birth",
                name="date_of_birth",
                type="date",
            ),

            # Номер телефона
            rx.text("Mobile Phone Number", size="3", font_weight="bold"),
            rx.input(
                placeholder="+7 (XXX) XXX-XX-XX",
                name="mob_phone",
                type="tel",
                pattern="[0-9+\-\s()]{10,20}",
                required=True,
            ),

            # Рабочий номер телефона
            rx.text("Work Phone Number", size="3", font_weight="bold"),
            rx.input(
                placeholder="+7 (XXX) XXX-XX-XX",
                name="work_phone",
                type="tel",
                pattern="[0-9+\-\s()]{10,20}", 
                required=False,
            ),

            # Образование
            rx.text("Choose your education level", size="3", font_weight="bold"),
            rx.select(
                ['Higher education', 'Secondary / secondary special','Incomplete higher','Lower secondary','Academic degree'],
                placeholder="Select option",
                name="education",
                required=True,
            ),

            # Тип дохода
            rx.text("What is your income type?", size="3", font_weight="bold"),
            rx.select(
                ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student', 'Other'],
                placeholder="Select option",
                name="income_type",
                required=True,
            ),

            # Доход
            rx.text("Annual income amount", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter your income amount",
                name="income_amount",
                type="number",
            ),

            rx.text("Date of Employment start", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter your date of employment start",
                name="date_of_emp",
                type="date",
            ),

            # Род деятельности
            rx.text("What is your occupation type?", size="3", font_weight="bold"),
            rx.select(
                ['Unknown','Security staff','Sales staff','Accountants','Laborers','Managers','Drivers','Core staff', 'High skill tech staff','Cleaning staff', 'Private service staff','Cooking staff','Low-skill Laborers','Medicine staff','Secretaries','Waiters/barmen staff','HR staff','Realty agents', 'IT staff'],
                placeholder="Select option",
                name="occupation",
                required=True,
            ),

            # Семейный статус
            rx.text("What is your marital status?", size="3", font_weight="bold"),
            rx.select(
                ['Civil marriage', 'Married', 'Single / not married', 'Separated', 'Widow'],
                placeholder="Select option",
                name="marital_status",
                required=True,
            ),

            # Количество детей
            rx.text("Number of family members", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter the number of family members",
                name="fam",
                type="number",
            ),

            # Количество детей
            rx.text("Number of children", size="3", font_weight="bold"),
            rx.input(
                placeholder="Enter the number of children",
                name="children",
                type="number",
            ),

            # Жилье
            rx.text("What is your housing type?", size="3", font_weight="bold"),
            rx.select(
                ['Rented apartment','House / apartment','Municipal apartment','With parents','Co-op apartment','Office apartment', 'Other'],
                placeholder="Select option",
                name="housing",
                required=True,
            ),
            
            # Собственность
            rx.text("Do you own any property?", size="3", font_weight="bold"),
            rx.select(
                ["Yes", "No"], 
                placeholder="Select option",
                name="property",
                required=True,
            ),
            
            # Автомобиль
            rx.text("Do you own a car?", size="3", font_weight="bold"),
            rx.select(
                ["Yes", "No"],  
                placeholder="Select option",
                name="car",
                required=True,
            ),
            
            rx.button(
                "Send application",
                type="submit",
                width="100%",
                background="#7ECEA7",
                color="white",
                _hover={
                    "transform": "scale(1.02)",
                    "box_shadow": "0 10px 20px rgba(0,0,0,0.2)",
                }
            ),
            rx.cond(
                State.show_result,
                rx.vstack(
                    rx.divider(),
                    rx.text(
                        f"Probability of credit card approval: {State.random_number}%",
                        size="6",
                        color="white",
                        font_weight="bold",
                    ),
                    rx.text(
                        "Thank you for your application!",
                        size="4",
                        color="white",
                    ),
                    spacing="2",
                    width="100%",
                    padding="10px",
                    bg="rgba(0,0,0,0.7)",
                    border_radius="10px",
                ),
                rx.box(), 
            ),
            spacing="4",
            width="100%",
        ),
        on_submit=State.handle_submit,
        width="100%",
        max_width="400px",
    )


class State(rx.State):

    random_number: int = 0
    show_result: bool = False

    def handle_submit(self, form_data: dict):
        """Обработчик отправки формы."""
        # name = form_data.get("name")
        # email = form_data.get("email")
        # gender = form_data.get("gender")
        # age = form_data.get("age")
        # date_of_bitrh = form_data.get("date_of_birth") 
        # mob_phone = form_data.get("mob_phone") 
        # work_phone = form_data.get("work_phone") 
        # property = form_data.get("property")
        # car = form_data.get("car")
        # education = form_data.get("education")
        # income_type = form_data.get("income_type")
        # income_amount = form_data.get("income_amount")
        # date_of_emp = form_data.get("date_of_emp")
        # occupation = form_data.get("occupation")
        # marital_status = form_data.get("marital_status")
        # children = form_data.get("children")
        # family = form_data.get("fam")
        # housing = form_data.get("housing")


        features = {
            'name': form_data.get("name"),
            'email': form_data.get("email"),
            'gender': form_data.get("gender"),
            'age': int(form_data.get("age")) if form_data.get("age") else None,
            'date_of_birth': form_data.get("date_of_birth"),
            'mob_phone': form_data.get("mob_phone"),
            'work_phone': form_data.get("work_phone"),
            'property': form_data.get("property"),
            'car': form_data.get("car"),
            'education': form_data.get("education"),
            'income_type': form_data.get("income_type"),
            'income_amount': float(form_data.get("income_amount")) if form_data.get("income_amount") else None,
            'date_of_emp': form_data.get("date_of_emp"),
            'occupation': form_data.get("occupation"),
            'marital_status': form_data.get("marital_status"),
            'children': int(form_data.get("children")) if form_data.get("children") else None,
            'family': form_data.get("fam"),
            'housing': form_data.get("housing"),
        }

        print(features)

        # features = {
        #         'age': int(self.age),
        #         'gender': self.gender,
        #         'salary': float(self.salary),
        #         'education': self.education
        #     }
        
        print(f"Получена заявка: {form_data.get("name")}, {form_data.get("email")}")

        self.random_number = random.randint(0, 100)
        self.show_result = True

        prediction = predict(features)
        print('Pred is:', prediction)


def index():
    return rx.hstack(
        rx.box(
            rx.image(
                src="/card.jpg",
                alt="Credit Card",
                width="100%", 
                height="auto",
            ),
            width="35%",
        ),
        rx.box(
            rx.vstack(
                rx.heading("Credit card application", size="9"),
                rx.text("Get a free credit card from our VeryImportant Bank (VIB)",size="5",),
                application_form(),
            ),
            width="65%",
            padding = '70px',
            padding_top = '70px',
        ),
        style={
            "background_image": "url('/font.jpg')",
            "background_size": "cover",
        },
        width="100%",
        spacing="0",
    )

app = rx.App()
app.add_page(index)
