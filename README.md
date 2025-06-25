# redis-supreme

A redis data admin.

This tool let's you see, modify and create redis data.

## Running behind Nginx

The repository contains a Next.js frontend and a FastAPI backend. Both services
can be proxied through Nginx so the site is served from a single entry point.

1. **Start the services**

   ```bash
   # Frontend on port 3000
   cd code/frontend
   npm install
   npm run build
   npm start &

   # Backend on port 8000
   cd ../backend
   pip install -r requirements.txt
   uvicorn app:app --host 0.0.0.0 --port 8000 &
   ```

2. **Create an Nginx server block**

   ```nginx
   server {
       listen 80;
       server_name example.com;

       location /api/ {
           proxy_pass http://localhost:8000/;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location / {
           proxy_pass http://localhost:3000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

   Place this configuration in `/etc/nginx/sites-available/redis-supreme` and
   enable it with:

   ```bash
   sudo ln -s /etc/nginx/sites-available/redis-supreme \
     /etc/nginx/sites-enabled/
   sudo nginx -s reload
   ```

The `/api/` prefix is forwarded to the backend, while all other traffic is sent
to the frontend.
