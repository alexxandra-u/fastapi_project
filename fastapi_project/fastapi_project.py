import reflex as rx
import random

from rxconfig import config
from .ml_model import predict


def application_form() -> rx.Component:
    """Форма подачи заявки на кредитную карту."""
    return rx.form(
        rx.vstack(
            rx.heading("Fill the form", size="5", margin_bottom="10px"),
            rx.grid(
                # Левая колонка
                rx.vstack(

                    # Имя
                    rx.hstack(
                        rx.text("Name", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.input(
                        placeholder="Enter your name",
                        name="name", 
                        required=True,
                        width="60%",
                    ),
                    
                    # Email
                    rx.hstack(
                        rx.text("Email", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.input(
                        placeholder="Enter your email",
                        name="email",
                        type="email",
                        required=True,
                        width="60%",
                    ),
                    
                    # Пол
                    rx.hstack(
                        rx.text("Gender", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ["Male", "Female", "Other"], 
                        placeholder="Select gender",
                        name="gender",
                        required=True,
                        width="60%",
                    ),

                    # День рождения
                    rx.hstack(
                        rx.text("Date of Birth", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.input(
                        placeholder="Enter your date of birth",
                        name="date_of_birth",
                        type="date",
                        width="50%",
                    ),

                    
                    # Номер телефона
                    rx.text("Mobile Phone Number", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.input(
                        placeholder="+7 (XXX) XXX-XX-XX",
                        name="mob_phone",
                        type="tel",
                        pattern=r"[0-9+\-\s()]{10,20}",
                        required=True,
                        width="60%",
                    ),
                    
                    # Рабочий номер телефона
                    rx.text("Work Phone Number", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.input(
                        placeholder="+7 (XXX) XXX-XX-XX",
                        name="work_phone",
                        type="tel",
                        pattern=r"[0-9+\-\s()]{10,20}",
                        required=False,
                        width="60%",
                    ),

                    # Семейный статус
                    rx.hstack(
                        rx.text("Marital status", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ['Civil marriage', 'Married', 'Single / not married', 'Separated', 'Widow'],
                        placeholder="Select option",
                        name="marital_status",
                        required=True,
                        width="80%",

                    ),
                    
                    # Количество членов семьи
                    rx.text("Number of family members", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.input(
                        placeholder="Enter the number of family members",
                        name="fam",
                        type="number",
                        width="80%",
                    ),
                    
                    # Количество детей
                    rx.text("Number of children", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.input(
                        placeholder="Enter the number of children",
                        name="children",
                        type="number",
                        width="80%",
                        margin_bottom="4px",
                    ),
                    
                    # Жилье
                    rx.text("Housing type", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.select(
                        ['Rented apartment','House / apartment','Municipal apartment','With parents','Co-op apartment','Office apartment', 'Other'],
                        placeholder="Select option",
                        name="housing",
                        required=True,
                        width="80%",
                        margin_bottom="4px",
                    ),
                    
                    spacing="2",
                    width="100%",
                ),
                
                # Правая колонка
                rx.vstack(
                    
                    # Доход
                    rx.text("Annual income amount", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.input(
                        placeholder="Enter your income amount",
                        name="income_amount",
                        type="number",
                        width="60%",
                    ),

                    # Тип дохода
                    rx.hstack(
                        rx.text("Income type", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student', 'Other'],
                        placeholder="Select option",
                        name="income_type",
                        required=True,
                        width="60%",
                        margin_bottom="4px",
                    ),

                    # Дата начала работы
                    rx.text("Date of Employment start", size="2", font_weight="bold", margin_bottom="2px"),
                    rx.input(
                        placeholder="Enter your date of employment start",
                        name="date_of_emp",
                        type="date",
                        width="50%",
                        margin_bottom="4px",
                    ),

                    # Род деятельности
                    rx.hstack(
                        rx.text("Occupation type?", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ['Unknown','Security staff','Sales staff','Accountants','Laborers','Managers','Drivers','Core staff', 'High skill tech staff','Cleaning staff', 'Private service staff','Cooking staff','Low-skill Laborers','Medicine staff','Secretaries','Waiters/barmen staff','HR staff','Realty agents', 'IT staff'],
                        placeholder="Select option",
                        name="occupation",
                        required=True,
                        width="60%",
                    ),

                    # Образование
                    rx.hstack(
                        rx.text("Education level", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ['Higher education', 'Secondary / secondary special','Incomplete higher','Lower secondary','Academic degree'],
                        placeholder="Select option",
                        name="education",
                        required=True,
                        width="60%",
                        margin_bottom="4px",
                    ),

                    # Собственность
                    rx.hstack(
                        rx.text("Do you own any property?", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ["Yes", "No"], 
                        placeholder="Select option",
                        name="property",
                        required=True,
                        width="50%",
                        margin_bottom="4px",
                    ),
                    
                    # Автомобиль
                    rx.hstack(
                        rx.text("Do you own a car?", size="2", font_weight="bold", margin_bottom="2px"),
                        rx.text("*", color="red", font_weight="bold", margin_bottom="2px"),
                        spacing="1",
                    ),
                    rx.select(
                        ["Yes", "No"],  
                        placeholder="Select option",
                        name="car",
                        required=True,
                        width="50%",
                        margin_bottom="4px",
                    ),
                    
                    spacing="2",
                    width="100%",
                ),
                
                columns="2",
                spacing="4",
                width="100%",
                margin_bottom="10px",
            ),
            
            rx.button(
                "Send application",
                type="submit",
                width="80%",
                background="#7ECEA7",
                color="white",
                _hover={
                    "transform": "scale(1.02)",
                    "box_shadow": "0 10px 20px rgba(0,0,0,0.2)",
                },
            ),

            rx.cond(
                State.is_loading,
                rx.vstack(
                    rx.spinner(
                        color="#7ECEA7",
                        size="2",
                    ),
                    rx.text(
                        "Processing your application...",
                        color="white",
                        font_weight="bold",
                    ),
                    spacing="2",
                    width="80%",
                    padding="20px",
                    bg="#5A9D7C",
                    border_radius="10px",
                    align="center",
                ),
                rx.box(),
            ),

            rx.cond(
                State.show_result,
                rx.vstack(
                    rx.text(
                        f"Probability of credit card approval: {round(State.prediction * 100, 2)}%",
                        size="5",
                        color="white",
                        font_weight="bold",
                    ),
                    rx.text(
                        "Thank you for your application!",
                        size="4",
                        color="white",
                    ),
                    spacing="2",
                    width="80%",
                    padding="10px",
                    bg="#5A9D7C",
                    border_radius="10px",
                ),
                rx.box(), 
            ),
            on_mount=State.on_mount,
            spacing="3",
            width="80%",
        ),
        on_submit=State.calc_pred,
        width="100%",
        max_width="800px",
    )


class State(rx.State):
    prediction: float = 0.0
    show_result: bool = False
    result: dict = {}
    error_message: str = ""
    is_loading: bool = False

    name: str = ""
    email: str = ""
    gender: str = ""
    date_of_birth: str = ""
    mob_phone: str = ""
    work_phone: str = ""
    property: str = ""
    car: str = ""
    education: str = ""
    income_type: str = ""
    income_amount: int = 0
    date_of_emp: str = ""
    occupation: str = ""
    marital_status: str = ""
    children: int = 0
    family: int = 0
    housing: str = ""

    def on_load(self) -> None:
        self.clear_form()

    def on_mount(self) -> None:
        self.clear_form()

    def clear_form(self) -> None:
        self.name = ""
        self.email = ""
        self.gender = ""
        self.date_of_birth = ""
        self.mob_phone = ""
        self.work_phone = ""
        self.property = ""
        self.car = ""
        self.education = ""
        self.income_type = ""
        self.income_amount = 0
        self.date_of_emp = ""
        self.occupation = ""
        self.marital_status = ""
        self.children = 0
        self.family = 0
        self.housing = ""
        

        self.prediction = 0.0
        self.show_result = False
        self.result = {}
        self.error_message = ""
        # self.is_loading = False

    def calc_pred(self, form_data: dict) -> dict:
        # self.is_loading = True
        features = {
            'name': form_data.get("name", ""),
            'email': form_data.get("email", ""),
            'gender': form_data.get("gender", ""),
            'date_of_birth': form_data.get("date_of_birth", ""),
            'mob_phone': form_data.get("mob_phone", ""),
            'work_phone': form_data.get("work_phone", ""),
            'property': form_data.get("property", ""),
            'car': form_data.get("car", ""),
            'education': form_data.get("education", ""),
            'income_type': form_data.get("income_type", ""),
            'income_amount': int(form_data.get("income_amount")),
            'date_of_emp': form_data.get("date_of_emp", ""),
            'occupation': form_data.get("occupation", ""),
            'marital_status': form_data.get("marital_status", ""),
            'children': int(form_data.get("children")),
            'family': int(form_data.get("fam")),
            'housing': form_data.get("housing", ""),
        }
        print(features['children'], type(features['children']))
        prediction = predict(features)
        print('Pred is:', prediction)

        self.prediction = prediction['score']
        # self.is_loading = False
        self.show_result = True

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