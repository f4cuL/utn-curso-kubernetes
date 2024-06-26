Parte 1 del TP de Kubernetes para el curso de Docker - Kubernetes

## Deployment

Para desplegar este proyecto primero se debe colocar en una consola de comandos ubicada sobre el proyecto la siguiente instrucción, 
```bash
  kubectl apply -f deployment.yml
```
![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/2bbd31b2-45a6-45cf-b096-0f179b1e3369)

Este comando generará los Pods de la aplicación, podemos validar que se generaron correctamente utilizando el comando 
```bash
  kubectl get pods
```
![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/9e5a9ee6-b189-4762-ba6c-0dd38346069f)

Podremos observar que se generaron dos replicas, por lo cual si eliminamos uno de estos pods, se generaran nuevamente.

## API Reference

| Endpoint |      Response     |
|----------|:-----------------:|
| /        | Bievenido al home |
| /hello   | Hola mundo!       |
| /goodbye | Adios mundo!      |


## Guia

Para utilizar la API debemos posicionarnos sobre alguno de los pods de la siguiente forma

```bash
  kubectl exec -it <"nombre_del_pod"> -- bash
```

![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/2051c9e3-d569-4e56-894e-773c6ed81f0d)

Una vez estamos ubicados en el pod con un bash, como el dockerfile instala en la imagen `curl` podemos utilizarlo dentro del pod de la siguiente forma

```bash
  curl <"url"> (Utilizar los endpoint de la API)
```
![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/7966830a-7e7a-4ccb-ba76-aa1ef537f7d9)

# Servicios
## NodePort

Para iniciar el servicio nodeport debemos ejecutar el comando
```bash
  kubectl apply -f nodeport.yml
```
 
Luego validamos que el servicio se creo correctamente utilizando 
```bash
  kubectl get svc nodeport-service
```
![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/8b8aff6c-3d8d-441f-ade9-9bb6af374da6)

o
```bash
  kubectl get all
```
![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/d4575c06-141a-419e-bf59-87c12e2e10ce)

y validamos que nuestra app se encuentra expuesta en el puerto 30000 como designamos en el yml

![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/87509258-17d4-4578-9bf9-43f8eb6b0edd)

## LoadBalancer

Para iniciar el servicio LoadBalancer debemos ejecutar el comando
```bash
  kubectl apply -f loadbalancer.yml
```

![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/d218c646-5fb0-4eec-a34c-1bd2eca1c4a6)

 
Luego validamos que el servicio se creo correctamente utilizando 
```bash
  kubectl get svc loadbalancer-service
```
![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/b7ae87c5-161e-4d76-b548-ed3d75db5602)


Utilizaremos curl para acceder a nuestro servidor mediante el uso del NodePort, para posteriormente revisar los logs de los pods y ver si el tráfico fue redirigido de forma equitativa entre los 2 pods

```bash
  curl localhost:30000
```

![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/e1e05385-6d81-419b-a815-8b03e96095f6)

```bash
  kubectl <"nombre del pod"> logs
```

![image](https://github.com/f4cuL/utn-curso-kubernetes/assets/56969887/895fbac5-3dc5-47b7-bc6a-79436823b639)

### Como se puede observar en la imagen, se realizaron 4 llamadas con curl al servidor, y el loadbalancer se encargo de dirigir el tráfico entre ambos pods, por lo que se utilizó 2 veces cada uno.







