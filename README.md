# Acknowledgementhub

This repository contains the Flask application for Acknowledgementhub.

## Setup and Installation

Follow these steps to get the application up and running on your local machine.

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/TEAM-AKH/Acknowledgementhub.git
cd Acknowledgementhub
```

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Once the virtual environment is activated, install the required Python packages:

```bash
pip install -r backend/requirements.txt
```

### 5. Set Environment Variables

The application requires certain environment variables for email functionality and security. Create a `.env` file in the `backend` directory or set these variables in your system environment:

- `MAIL_USERNAME`: Your email address for sending emails (e.g., a Gmail address).
- `MAIL_PASSWORD`: The app password for your email account (if using Gmail, you'll need to generate one).
- `SECRET_KEY`: A strong, random string for Flask session management.

Example `.env` file content (in `backend/.env`):

```
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_app_password
SECRET_KEY=super_secret_key_here
```

### 6. Run the Application

Navigate to the `backend` directory and run the Flask application:

```bash
cd backend
python app.py
```

The application will typically run on `http://127.0.0.1:5000`.

### 7. Access Admin Panel (Optional)

If you need to access the admin panel, an admin user is automatically created if it doesn't exist with the following credentials:

- **Username:** `admin`
- **Password:** `adminpass`

You can access the admin panel at `http://127.0.0.1:5000/admin`.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.