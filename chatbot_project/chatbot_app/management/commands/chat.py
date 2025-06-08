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
                'chatterbot.logic.TimeLogicAdapter',
                'chatterbot.logic.MathematicalEvaluation'
            ],
            database_uri='sqlite:///db.sqlite3'
        )

        # Train on English corpus; comment out after first run to persist memory
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train('chatterbot.corpus.english')

        self.stdout.write(self.style.SUCCESS(
            'Chat session started! (Type "exit" to quit or Ctrl-C to exit)\n'
        ))

        # Start conversation with Chatterbot
        while True:
            try:
                user_input = input('You: ').strip()
                if not user_input:
                    continue
                if user_input.lower() == 'exit':
                    self.stdout.write('\nGoodbye!')
                    break

                response = chatbot.get_response(user_input)
                self.stdout.write(f'Bot: {response}')
            except (KeyboardInterrupt, EOFError):
                self.stdout.write('\nGoodbye!')
                break

        self.stdout.write('Exiting chat.')
        sys.exit(0)
