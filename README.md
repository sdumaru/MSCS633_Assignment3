# Django Terminal ChatBot with ChatterBot

A terminal-based chatbot implementation using Django's management commands and ChatterBot's machine learning dialog engine. Users can interact with an AI agent trained on the English corpus directly from the command line.

---

## Installation and Running the program

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sdumaru/MSCS633_Assignment3.git
   cd chatbot_project

2. **Prerequisites:** Before you begin, make sure you have **Python 3.8+** and **pip** installed. Then install language models and required packages:

    ```bash
    py -m pip install Django==5.2.2
    pip install chatterbot
    pip install chatterbot-corpus
    python -m spacy download en_core_web_sm
    pip install pyyaml

3. **Apply Django migrations:**
    ```bash
    python manage.py migrate

4. **Run the chat app:**
    ```bash
    python manage.py chat

## References

- [Writing your first Django app](https://docs.djangoproject.com/en/5.2/intro/tutorial01/) – Django documentation
- [ChatterBot setup guide](https://docs.chatterbot.us/setup/) – ChatterBot documentation
- [Install packages for Django integration](https://docs.chatterbot.us/django/#install-packages) – ChatterBot documentation
- [ChatterBot Django settings](https://docs.chatterbot.us/django/settings/) – ChatterBot documentation
- [ChatterBot examples](https://docs.chatterbot.us/examples/) – ChatterBot documentation
- [Example API views (Django integration)](https://docs.chatterbot.us/django/views/#example-api-views) – ChatterBot documentation