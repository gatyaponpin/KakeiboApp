# 環境構築方法２

## 1.POSTGRESQLの設定

docker-compose run --rm backend bash

```settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kakeibo',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

python manage.py migrate

docker compose down
docker compose up --build

## 2.書き込み権限設定（適宜）

sudo chown $USER:$USER /home/einoshin/Develop/Deliverables/KakeiboV2/backend/config/settings.py

## 3.Vue Router と Pinia のインストールとセットアップ

cd frontend
npm install vue-router pinia

```src/router/index.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '@/views/Home.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

```src/store/index.ts
import { createPinia } from 'pinia'

const pinia = createPinia()
export default pinia
```

## 4.TypeScript使用に変換

cd frontend
npm install --save-dev typescript
mv src/main.js src/main.ts
npm install --save-dev @types/node
npx tsc --init
mv vite.config.js vite.config.ts