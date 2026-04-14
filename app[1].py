"""
Main application entry point
"""
import sys
import logging
import customtkinter as ctk
from src.views.login_view import LoginView
from src.controllers.auth_controller import AuthController
from src.utils.database import create_database

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting Hospital Management System")
        
        # Initialize database and tables
        create_database()
        
        # Create default admin account if it doesn't exist
        AuthController.create_admin_if_not_exists()
        
        # Initialize customtkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create and start login view
        app = LoginView()
        app.mainloop()
        
        logger.info("Application closed")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()