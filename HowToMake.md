# 環境構築方法

## 1.ディレクトリ構成

```txt
kakeibo-app/
├── backend/           # Django アプリケーション
├── frontend/          # Vue 3 アプリケーション
├── nginx/             # リバースプロキシ
├── docker-compose.yml
└── README.md
```

## 2.Docker & docker-compose.yml を作成

```docker-compose.yml
version: "3.9"
services:
  backend:
    build: ./backend
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    volumes:
      - ./frontend:/app
    command: npm run dev -- --host

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: kakeibo
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## 3.バックエンドのセットアップ

```Dockerfile
FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

```requirements.txt
Django>=4.2
djangorestframework
psycopg2-binary
```

- バックエンドマシンで Django プロジェクトを作成する

docker-compose run --rm backend bash
django-admin startproject config .

## 4.フロントエンドのセットアップ

```Dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
CMD ["npm", "run", "dev", "--", "--host"]
```

- フロントマシンで Vue を作成する

npm create vite@latest . -- --template vue
npm install

## 6.初回ビルドと起動

docker-compose up --build

- Vue: <http://localhost:5173>
- Django: <http://localhost:8000>
