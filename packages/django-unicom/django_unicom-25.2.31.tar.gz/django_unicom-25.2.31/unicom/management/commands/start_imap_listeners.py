from django.core.management.base import BaseCommand
from unicom.services.email.IMAP_thread_manager import imap_manager
import time
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Start IMAP listeners for all active email channels and keep them running"

    def handle(self, *args, **options):
        self.stdout.write("Starting IMAP listeners for all active email channels...")
        imap_manager.start_all()
        self.stdout.write(self.style.SUCCESS("IMAP listeners started successfully"))
        
        try:
            self.stdout.write("Press Ctrl+C to stop...")
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            self.stdout.write("\nShutting down IMAP listeners...")
            self.stdout.write(self.style.SUCCESS("IMAP listeners stopped"))