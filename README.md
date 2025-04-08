# Google+ Clone

A modern social networking platform built with Django and Angular.

## Features

- User authentication and authorization
- Profile management
- Posts and comments
- Circles (friend groups)
- Real-time notifications
- Photo sharing
- Search functionality

## Tech Stack

- Backend: Django + Django REST Framework
- Frontend: Angular
- Database: PostgreSQL
- Authentication: JWT

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/googleplus_clone
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

### Frontend Setup

1. Install Node.js and npm

2. Install Angular CLI:
```bash
npm install -g @angular/cli
```

3. Navigate to the frontend directory:
```bash
cd frontend
```

4. Install dependencies:
```bash
npm install
```

5. Start the development server:
```bash
ng serve
```

## API Documentation

The API documentation is available at `/api/docs/` when running the development server.

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
