# Kubernetes-Lab
## Запуск
```bash
minikube start --driver=docker

docker build -t backend:1.0.0 ./backend
docker build -t frontend:1.0.0 ./frontend
minikube image load backend:1.0.0
minikube image load frontend:1.0.0

kubectl apply -f k8s/
kubectl get deployments
kubectl get pods
kubectl get services
```

## Доступ снаружи кластера
```bash
minikube service frontend-service --url
```
Открыть выведенный адрес в браузере, но терминал не закрывать

## Тестирование
1. Открыть адрес frontend в браузере: должен отображаться ответ вида
   `FRONTEND pod: ... | backend answered: Hello from BACKEND, pod: ...`
2. Обновить страницу несколько раз: имя backend pod'а меняется.
3. Самовосстановление:
```bash
kubectl delete pod <имя backend pod'а>
kubectl get pods
```
4. Масштабирование:
```bash
kubectl scale deployment backend-deployment --replicas=5
kubectl get pods
```

## Остановка и очистка
```bash
kubectl delete -f k8s/
minikube stop
```
