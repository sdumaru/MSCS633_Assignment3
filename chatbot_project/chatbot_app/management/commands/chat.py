# References:
# https://pypi.org/project/ChatterBot/
# https://docs.chatterbot.us/examples/
# https://docs.chatterbot.us/training/

import sys
from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Command(BaseCommand):
    help = 'Run an interactive terminal chat session with ChatterBot'

    def handle(self, *args, **options):
        # Initialize ChatBot instance
        chatbot = ChatBot(
            'TerminalChatBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.BestMatch',
                'chatterbot.logic.TimeLogicAdapter',            # For time
                'chatterbot.logic.MathematicalEvaluation'       # For mathematical operation
            ],
            database_uri='sqlite:///db.sqlite3'
        )

        # Train on English corpus
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train('chatterbot.corpus.english')

        # Start chat session with success style message (green)
        self.stdout.write(self.style.SUCCESS(
            'Chat session started! (Type "exit" to quit or Ctrl-C to exit)\n'
        ))

        # Start conversation with Chatterbot continuously
        while True:
            try:
                user_input = input('You: ').strip()
                # Make sure user input something to get response from bot
                if not user_input:
                    continue

                # Exit the chat session with exit command
                if user_input.lower() == 'exit':
                    self.stdout.write('\nGoodbye!')
                    break

                response = chatbot.get_response(user_input)
                self.stdout.write(f'Bot: {response}')

            # Exit with Ctrl + D command    
            except (KeyboardInterrupt, EOFError):
                self.stdout.write('\nGoodbye!')
                break

        # End chat session with error style message (red)
        self.stdout.write(self.style.ERROR('Exiting chat!!!'))
        sys.exit(0)
