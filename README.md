# 🌶️ SpiceCraft (Pickle Mini Project)

Welcome to the **SpiceCraft** (Pickle Mini Project) repository! This is a dynamic, fully-featured full-stack web application designed for a premium Indian pickle business.

## 🚀 Key Features
- **Beautiful UI:** Developed with modern glassmorphism aesthetics, Google Fonts ('Outfit'), FontAwesome icons, CSS variables and fully responsive layout using Bootstrap.
- **Admin Dashboard:** Admins can securely add, edit, and delete pickles in the database. Images are dynamically securely uploaded via Cloudinary.
- **Frontend Catalog:** Browse beautiful cards showcasing the catalog of premium pickles.
- **Authentication:** JWT-based protection, ensuring user/admin specific routes are securely handled via FastAPI.
- **Shopping Cart:** Authenticated users can browse the shop and manage their cart.

## 🛠️ Technology Stack
- **Backend:** FastAPI (Python), PyMongo, PassLib, python-jose (JWT)
- **Database:** MongoDB
- **Image Storage:** Cloudinary
- **Frontend:** HTML5, Vanilla CSS3 (Custom Glassmorphism styling), Bootstrap 5, Vanilla JS

---

## 💻 How to Start the Project Locally

### 1️⃣ Setup the Python Environment
Ensure you have Python installed. It's recommended to work within a virtual environment.

```bash
# 1. Provide a virtual environment (if not already set up)
python -m venv .venv

# 2. Activate the virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 3. Install backend requirements
pip install -r requirements.txt
# (or pip install fastapi uvicorn pymongo python-multipart passlib[bcrypt] python-jose cloudinary)
```

### 2️⃣ Start the Backend Server (FastAPI)
The backend requires `uvicorn` to run the FastAPI app locally. Start it using the following command inside the root folder:

```bash
# Start the uvicorn server on host 127.0.0.1 port 8000
uvicorn backend.main:app --reload
```
You should see: `Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`

You can view the fully interactive **API Documentation** generated automatically at:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3️⃣ Initialize the Admin Account (First time only)
Since the `Admin Dashboard` is secured, you'll need an initial Admin account.
- While the backend is running, open a browser and go to:  
  👉 [http://127.0.0.1:8000/users/create-admin/](http://127.0.0.1:8000/users/create-admin/)  
- *This is a one-time execution route that populates the database with default admin credentials (`admin@pickle.com` / `admin123`).*

### 4️⃣ Start the Frontend
Since the frontend uses basic API fetch requests, you don't necessarily need a development server like Node. However, it is **highly recommended** to use a simple HTTP server to avoid CORS issues for local development.

```bash
# Start a simple HTTP server for the frontend folder
cd frontend
python -m http.server 3000
```
- Open your browser to: 👉 [http://localhost:3000](http://localhost:3000)

**Without a server (Direct file access)**:  
Alternatively, simply double-click `frontend/index.html` to open it in your browser (`file:///C:/.../index.html`). The login, requests, and browsing functions have been designed to fetch absolute backend links so they will run out-of-the-box.

---

## 🎨 User Guide

### Accessing the Store as a Customer
1. Navigate to the `index.html`.
2. Click **Login** / **Sign Up** to create a user account.
3. Browse the rich, animated product catalog and add things to your cart.

### Accessing the Store as an Admin
1. Once your default Admin is created via the setup step, go to `login.html`.
2. Login with:
   - **Email:** `admin@pickle.com`
   - **Password:** `admin123`
3. Upon success, navigate to `admin.html`. Here you are granted powers to Add, Update, and Remove products from the universal database!

## 🔧 Database Details & Cloud Configurations
- MongoDB URI & DB configuration is located securely internally at `backend/config.py`.
- Image Upload setup uses a pre-configured Cloudinary keyset in `backend/config.py`. When an image is added via the dashboard, it is piped seamlessly to the cloud and its secure URL is stored directly inside MongoDB.
