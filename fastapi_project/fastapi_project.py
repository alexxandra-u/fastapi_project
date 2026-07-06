"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random

from rxconfig import config


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
        name = form_data.get("name")
        email = form_data.get("email")
        gender = form_data.get("gender")
        age = form_data.get("age")
        property = form_data.get("property")
        car = form_data.get("car")
        
        print(f"Получена заявка: {name}, {email}")

        self.random_number = random.randint(0, 100)
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
