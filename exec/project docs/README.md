# π Build & λ°°ν¬ λ¬Έμ

## π λ²μ  μ λ³΄ λ° μ€μ  μ λ³΄

- JVM λ²μ  :  1.8
- μΉ μλ² : AWS λ°°ν¬
- WAS : Apache Tomcat
- Intellij : 2020.2
- PyCharm : 2021.2
- Kotlin : 1.5.21
- Android : min SDK 24
- Swift : 5

## π Build λ° λ°°ν¬ μ½λ

### βοΈ Spring

- Spring νλ‘μ νΈ μμ Dockerfile νμΌμ λ§λ€κ³  μλ μ½λλ₯Ό μλ ₯νλ€.

```java
FROM openjdk:8-jdk-alpine
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

- gradlew νμΌμ΄ μλ λλ ν°λ¦¬μμ μλ λͺλ Ήμ΄λ₯Ό μ°¨λ‘λλ‘ μλ ₯νλ€.

```bash
$ sudo ./gradlew clean

$ sudo ./gradlew build
```

- λ€μ build λλ ν°λ¦¬κ° μλ μμΉ(spring νλ‘μ νΈμ μ΅μλ¨)μμ μλ λͺλ Ήμ΄λ₯Ό μλ ₯νλ€.

```bash
$ docker build -t [μ΄λ―Έμ§μ΄λ¦] .
```

- λ€μ μ½λλ₯Ό κ³μν΄μ μμλλ‘ μλ ₯νλ€.
- μ¬κΈ°μ λμ»€νλΈ μμ΄λλ μ΄λ©μΌμ΄ μλ Dockerμ μμ΄λλ₯Ό μλ―Ένλ€.

```bash
$ docker tag [μ΄λ―Έμ§ μ΄λ¦]:latest [λμ»€νλΈμμ΄λ]/[μ΄λ―Έμ§μ΄λ¦]:latest

$ docker push [λμ»€νλΈμμ΄λ]/[μ΄λ―Έμ§μ΄λ¦]:latest
```

- μλ λ‘μ»¬μμ μ§νν κ²μ΄κ³  μ΄μ  EC2 μλ²μμ μ§ννλ€.
- λ¬΄μ€λ¨ μ€νμ ν¬νΈλ²νΈλ λ°λμ λμ»€ ν¬νΈμ μ΄λ―Έμ§ ν¬νΈ 2κ°λ₯Ό μ€μ ν΄μΌμ§ μ μ μ€νλλ€!

```bash
# EC2 μλ²μμ
$ sudo docker pull [λμ»€νλΈμμ΄λ]/[μ΄λ―Έμ§μ΄λ¦]:latest

# λ¬΄μ€λ¨ μ€ν
$ docker run -d -p [μ¬μ©ν  ν¬νΈ] [λμ»€μ΄λ―Έμ§Name]

# μμ (μν¬νΈ = λμ»€ ν¬νΈ / λ·ν¬νΈ = μ΄λ―Έμ§ ν¬νΈ)
$ sudo docker run -d -p 8080:8080 youn0729/damhwa:latest
```

### βοΈ Django Version

```
Django νλ‘μ νΈλ₯Ό Docker Imageλ‘ λΉλνμ¬ EC2 μΈμ€ν΄μ€μ λ°°ν¬νλ κ²
Docker μ€μΉ, Docker Hub κ³μ  μμ±, Django νλ‘μ νΈ μμ±μ΄ λμ΄ μμ΄μΌ νλ€.
```

- λ§μ΄κ·Έλ μ΄μ μ§ννλ€.

```bash
python manage.py makemigrations

pythom manage.py migrate
```

- requirements.txt λ₯Ό μμ±νλ€.
- μ¦ pipλ‘ install λ νκ²½μ txt νμΌμ μ μ₯νμ¬ Dockerμμλ λμΌνκ² κ΅¬μ±νλλ‘ νλ κ²μ΄λ€.

```bash
pip freeze > requirements.txt
```

### βοΈ Dockerfile μμ±

- Django νλ‘μ νΈ μ΅μλ¨μ Dockerfile μ΄λΌλ μ΄λ¦μΌλ‘ νμΌμ μμ±νλ€. (λ°λμ νμΌλͺμ΄ νλ¦¬λ©΄ μλ¨!)
- Django νλ‘μ νΈ μ΅μλ¨μ΄λΌλ κ²μ λ€μ λ§ν΄μ manage.pyκ° μλ κ²½λ‘λ₯Ό λ§νλ κ²μ΄λ€.

```python
FROM python:3 # μμ±νλ Dockerμ python λ²μ 
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN apt-get -y install vim # Docker μμμ vi μ€μΉ μν΄λ λ¨

RUN mkdir /srv/docker-server # Dockerμμ srv/docker-server ν΄λ μμ±
ADD . /srv/docker-server # νμ¬ λλ ν°λ¦¬λ₯Ό srv/docker-server ν΄λμ λ³΅μ¬

WORKDIR /srv/docker-server # μμ λλ ν°λ¦¬ μ€μ 

RUN pip install --upgrade pip # pip μκ·Έλ μ΄λ
RUN apt-get install build-essential
RUN pip install --upgrade pip setuptools wheel # Transformers μ€μΉ μλ¬ λ°©μ§
RUN pip install -r requirements.txt --no-cache-dir # Python torch μ€μΉ μλ¬ λ°©μ§

EXPOSE 8000 # 8000 port κ°λ°©
CMD ["python","manage.py","runserver","0.0.0.0:8000"] # μ€ν
```

### βοΈ Docker image μμ±

- νμ¬ κ²½λ‘μμ Docker image buildλ₯Ό μ§ννλ€.

```bash
docker build -t [μμ±νκ³ μ νλ λμ»€ μ΄λ―Έμ§μ΄λ¦] .
```

- μ΄λ―Έμ§κ° μ μμ μΌλ‘ λ§λ€μ΄μ‘λμ§ νμΈνκΈ° μν΄ docker imagesλ₯Ό μλ ₯

```bash
docker images
```

- μ΄μ  μ λλ‘ λμκ°λμ§ νλ² λλ €λ³΄μ

```bash
docker run -p [νΈμ€νΈν¬νΈ]:[μ»¨νμ΄λν¬νΈ] [μμ±ν μ΄λ―Έμ§ μ΄λ¦]

# μμ
docker run -p 8000:8000 damhwa_django
```

- λ§μ½ λ°±κ·ΈλΌμ΄λμμ μ€ννκ³  μΆμ λλ μλμ²λΌ νλ€.

```bash
docker run -d -p [νΈμ€νΈν¬νΈ]:[μ»¨νμ΄λν¬νΈ] [μμ±ν μ΄λ―Έμ§ μ΄λ¦]

# μμ
docker run -d -p 8000:8000 damhwa_django
```

- λ§μ½ μμμ μ λλ‘ μ€ν λμλ€λ©΄ μ΄μ  Docker νλΈμ push ν΄μ EC2 μλ²μμ λΆλ¬μλ³΄μ

### π Docker Hub μ Image νμΌ Push νκΈ°

- Docker Hub κ³μ μ΄ λ°λμ μμ΄μΌ νλ€.
- μλ λͺλ Ήμ΄λ‘ push ν΄λ³΄μ

```bash
docker tag [μμ±ν μ΄λ―Έμ§ μ΄λ¦]:latest [λμ»€νλΈμμ΄λ]/[μμ±ν μ΄λ―Έμ§ μ΄λ¦]:latest

docker push [λμ»€νλΈμμ΄λ]/[μμ±ν μ΄λ―Έμ§ μ΄λ¦]:latest
```

- μ΄μ  Docker νλΈλ₯Ό νμΈν΄λ³΄λ©΄ ν΄λΉ μ΄λ―Έμ§κ° μ¬λΌκ°μμ κ²μ΄λ€.

### π EC2 μλ²μμ pull λ°μ μ€ννκΈ°

- μ΄μ  Docker Hubμμ μ΄λ―Έμ§λ₯Ό κ°μ Έμ λ°±κ·ΈλΌμ΄λλ‘ μ€νμν€λ©΄ λ!
- μ¬μ©ν  μ»¨νμ΄λμ λ³μΉ­μ μ§μ ν΄μ£Όλ©΄ ν΄λΉ μ»¨νμ΄λμ IDλ₯Ό λ΄κ° μ§μ ν λ³μΉ­μΌλ‘ μ¬μ©ν  μ μλ€.

```bash
docker pull [λμ»€νλΈμμ΄λ]/[μμ±ν μ΄λ―Έμ§ μ΄λ¦]:latest

docker run -d -p [νΈμ€νΈν¬νΈ]:[μ»¨νμ΄λν¬νΈ] [μμ±ν μ΄λ―Έμ§ μ΄λ¦]

docker run -d -p 8000:8000 --name [μ¬μ©ν  μ»¨νμ΄λλ³μΉ­][μμ±ν μ΄λ―Έμ§ μ΄λ¦]

# μμ
docker run -d -p 8000:8000 damhwa_django
```

## β οΈ λ°°ν¬ μ νΉμ΄μ¬ν­

- Django μλ²μ Spring μλ² λ λ€ λ°°ν¬
- Django μλ² ν¬νΈ : 8000
- Spring μλ² ν¬νΈ : 8080
- Docker Hubλ‘ λ°°ν¬ μ±κ³΅

## π DB μ λ³΄

- λ°°ν¬μ© DB μ λ³΄

  -> Hostname(μ μ μ£Όμ) : 3.38.83.30 / λλ©μΈ : j5a503.p.ssafy.io

  -> Username : ssafy

  -> UserPassword : ssafy
  
  ![αα³αα³αα΅α«αα£αΊ 2021-10-05 αα©αα? 10 18 49](https://user-images.githubusercontent.com/48318620/136031000-7f4530d3-8496-4a4c-b4c7-9dc3f35c05b0.png)


- ER-Diagram

    <img width="901" alt="αα³αα³αα΅α«αα£αΊ 2021-10-05 αα©αα? 10 23 16" src="https://user-images.githubusercontent.com/48318620/136031526-93cf4322-3d21-4dd1-b8bf-a506ea143bec.png">

    
## π μΈκ³΅μ§λ₯ Model

- SKT Brain KoBERT Model : νκ΅­μ΄ λ²μ μ μμ°μ΄ μ²λ¦¬ λͺ¨λΈ
- λ³Έ νλ‘μ νΈμμ μ§νν νμ΅μ κΈ°μ‘΄μ νμ΅λ KoBERT λͺ¨λΈμ κ°μ  μΈμ΄λ₯Ό μ£Όμνλ Fine Tuningμ΄λ€.
- AIhubμ μ¬λΌμ μλ μ½ 7λ§μ¬κ°μ νκ΅­μ΄ λ§λ­μΉ λ°μ΄ν°λ₯Ό νμ΅νμ¬ μ΄ 6κ°μ κ°μ  λλΆλ₯ λͺ¨νμ λ§λ€μλ€.
- testλ°μ΄ν°λ‘ μ±λ₯μ μΈ‘μ ν κ²°κ³Ό μ½ 86%μ μ νλλ₯Ό μ§λκ³  μλ€.
- KoBERTλ₯Ό μ΄μΌκΈ° νκΈ°μ μ BERTμ λν΄μ μ‘°κΈ λ μ€λͺνμλ©΄ μλμ κ°λ€.

#### π€ BERTμ λν κΈ°λ³Έμ μΈ μ€λͺ

- μμ°μ΄ μ²λ¦¬ λΆμΌμμ 2019λμ ν νμ μ§μ μμ²­λ μ±λ₯μ μ§λ λͺ¨λΈμ΄ λμμΌλ©°. κ·Έκ² λ°λ‘ BERTμ΄λ€.
- BERTλ Bidirectional Encoder Representations from Transformerμ μ½μλ‘ νμ€νΈλ₯Ό μλ°©ν₯(μλ€)λ‘ νμΈνμ¬ μμ°μ΄λ₯Ό μ²λ¦¬νλ λͺ¨λΈμ΄λ€. κΈ°μ‘΄μ μμ°μ΄ μ²λ¦¬ λͺ¨λΈμ λ¨λ°©ν₯ μ°λ¦¬κ° κΈμ μ½λ μμμΈ μΌμͺ½βμ€λ₯Έμͺ½μΌλ‘ κ°μ§λ§ BERTλ μ΄ μμλ₯Ό μλ°©ν₯μΌλ‘ λ³΄κΈ° λλ¬Έμ λ€λ₯Έ λͺ¨λΈμ λΉν΄ λ§€μ° λμ μ νλλ₯Ό λνλΈλ€. κ·Έλ¦¬κ³  λ¬΄μλ³΄λ€ λν μΈκ³΅μ§λ₯μ μΌμ’(κ΅¬κΈμμ κ°λ°)μ΄κ³  μ€νμμ€μ΄κΈ° λλ¬Έμ λκ΅¬λ μ¬μ©ν  μ μλ μ₯μ μ΄ μλ€.
- λ³Έ νΉν νλ‘μ νΈμμλ μΈκ³΅μ§λ₯ λͺ¨λΈ κ΅¬μΆμμ Colabμ νμ©νκ³  GPUλ₯Ό ν΅ν΄ λͺ¨λΈ νμ΅μ κ±Έλ¦° μκ°μ 2μκ°μ΄λ©° νλμ λͺ¨λΈμ κ΅¬μΆνλλ° λ§μ μκ°μ΄ κ±Έλ¦°λ€. λ°λΌμ Colab νκ²½μμ μ§μνλ GPU λλ TPUλ₯Ό μ¬μ©νμ. CPUλ‘ μ°μ°μ μννλ©΄ μμ μ§νλμ§ μμμ λλλ€.
- κ·Έλ¦¬κ³  KoBERTλΌλ κ²μ νκ΅­μ΄μ κ²½μ° λ€λ₯Έ λλΌμ μΈμ΄λ³΄λ€ ν¨μ¬ λ³΅μ‘ν΄μ SKT-brainμμ BERTμ νκ΅­μ΄ λ²μ μ λ§λ€μλ€. μμΈ‘λ₯ μ΄ ν¨μ¬ μ’λ€κ³ νλ€. νΉν κ΄λ ¨ μ΄μλ₯Ό [https://github.com/SKTBrain/KoBERT/pulls?q=is%3Apr+is%3Aclosed](https://github.com/SKTBrain/KoBERT/pulls?q=is%3Apr+is%3Aclosed) μμ κ²μνμ¬ ν΄κ²°ν  μ μμΌλ μ°Έκ³ νλ©΄ λλ€.
- BERTλ₯Ό νμ΅νκΈ° μν΄μ μ¬μ©ν λΌμ΄λΈλ¬λ¦¬λ `kobert, pytorch`μ΄λ€.

##### βοΈ Colabνκ²½μμ KoBERT νμ΅νκΈ°

```bash
!pip install mxnet # μ½λ© νκ²½μ΄κΈ° λλ¬Έμ μμ !λ₯Ό λΆμ¬μΌ νλ€.
!pip install gluonnlp pandas tqdm
!pip install sentencepiece
!pip install transformers==3.0.2
!pip install torch
```

KoBERTλ₯Ό μ΄μ©νκΈ° μν΄μλ κΈ°λ³Έμ μΌλ‘ μμ κ°μ λΌμ΄λΈλ¬λ¦¬κ° μμ΄μΌ νλ€. νΉν KoBERTμμλ  mxnet, torch, gluonnlpλ₯Ό νν λ€μ΄λ‘λ λ°μμΌ νλ©°, BERT λͺ¨λΈ κ³΅ν΅μ μΌλ‘ transformers λΌμ΄λΈλ¬λ¦¬κ° μμ΄μΌ νλ€. λν python λ²μ μ λ°λΌ μλνλ transformersμ λ²μ μ΄ μμ΄νλ―λ‘ μ΄λ₯Ό μ£Όμνμ. λ³Έ νΉν νλ‘μ νΈμμλ python==3.7.xμ transformers==3.0.2λ₯Ό μ¬μ©νλ€. κ·Έλμ μμ κ°μ΄ λ€μ΄λ‘λλ₯Ό λ°μμ€λ€.

λν λ§μ½μ λ΄κ° KoBERTλ₯Ό μ΄μ©νλ κ²μ΄λ©΄

```bash
!pip install git+https://git@github.com/SKTBrain/KoBERT.git@master
```

μμ μ½λλ‘ KoBERT λΌμ΄λΈλ¬λ¦¬λ₯Ό μ¬μ©νκΈ° μν ν¨ν€μ§λ₯Ό λ€μ΄λ‘λ λ°μμΌνλ€.

```python
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook
```

νμν ν¨μλ₯Ό λͺ¨λ loadν΄μ€λ€. λλ μμ μλ λͺ¨λ  ν¨μμ μλ―Έλ₯Ό μμ§λ λͺ»νλ€. λ¨μ§ KoBERTλ₯Ό μ΄μ©νκΈ° μν΄ μμμ λ―Έλ¦¬ μ€μ ν΄μΌ ν  ν¨μλ€μ΄λ€.

```python
#kobert
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

#transformers
from transformers import AdamW # μΈκ³΅μ§λ₯ λͺ¨λΈμ μ΄κΈ°κ° μ§μ  ν¨μλ₯Ό μλ΄μΌλ‘ μ§μ νλ€.
from transformers.optimization import get_cosine_schedule_with_warmup
```

kobert λΆλΆμ μ°λ¦¬κ° νμ΅ν  Kobert λͺ¨λΈμ λΆλ¬μ€κΈ° μν΄ μ€μ νλ κ²μ΄λ€. μλ μ°λ¦¬κ° μΈκ³΅μ§λ₯μ λ§λ€λλ°, μ μ λ°κ±Έ μ€μ ν΄? λΌκ³  μκ°νλ€λ©΄, μΌλ¨ BERT λͺ¨ν μμ²΄κ° μ€νμμ€λ€. μ΄λ―Έ κ΅¬κΈμμ 104κ°μ μΈμ΄λ₯Ό κ΅¬λΆν΄μ νμ΅ν μΈμ΄ λͺ¨λΈμ΄λ€. κ·Έλ λ€ μ΄λ―Έ νμ΅νλ€. κ·Έκ±Έ μ°λ¦¬κ° κ°μ Έλ€κ° μ°λκ±°λ€. κ·Έλ¬λ©΄ λ¬΄μμ νμ΅νλκ°? μλ§ ν λλΌμ μΈμ΄λ³ νΉμ§μ νμ΅νμ§ μμλ μκ°λ λ€. κ³΅μλ¬Έμ λ€μ΄κ°μ νμΈν΄λ³΄λ©΄ λκ² λ€.

κ·Έλ¦¬κ³  BERT λͺ¨νμ νμ±ν ν¨μλ₯Ό softmaxν¨μλ₯Ό μ¬μ©νλ€. κ·Έλμ μλ ₯κ°μΌλ‘ μΈν΄ μΆλ ₯λ κ°μ λͺ¨λ 0~1μ¬μ΄μ κ°μ΄κ³  λ€ λ νμ λ 1μ΄λλ€. κ·Έλ λ€ κ·Έλ₯ νλ₯ μ΄λ€.

(μλ°ν νλ₯ μ΄λ? λΌκ³  νμ λ κ·Έλ κ² λ΄λ λ¬΄λ°©νλ€. μ΄μ°¨νΌ μΈκ³΅μ§λ₯λ weightλΆλΆμ λͺ¨μλ‘ μΆμ νλ€. κ·Έλ¦¬κ³  μ΄λ₯Ό κ²½μ¬νκ°λ²μ ν΅ν΄ μ΅μ μ weightμ μ°Ύλκ±΄λ°, μ΄λ μ΄ weightμ νλ₯ λ³μλ‘ λ³Έλ€. κ·Έλ λ€ κ·Έλ₯ νλ₯ μ΄λ€.)

```python
#GPU μ¬μ©
device = torch.device("cuda:0")
```

μΈκ³΅μ§λ₯μ GPUμμΌλ©΄ κ·Έλ₯ λ€νμλ κ°λ€. μ°μ°μ΄ μλͺ CPUλ‘ νμ§λ§μ 1λμ΄ λμ΄λ μλλ  μ μλ€. κ·ΈλκΉ GPU μ¬μ©μ μ€μ ν΄μ£Όμ. μ£Όλ³ μ΄μΌκΈ°λ‘λ TPUλ₯Ό μ°λΌκ³  νλλ°, TPUλ₯Ό μ°λ©΄ μ½λκ° μ’ λ¬λΌμ§λ€. κ·Έλμ μΌλΆλ¬ GPUλ‘ λ¨Όμ  μ²΄ννλ μμΌλ‘ μ¬μ©ν΄λ³΄μ.

λμΉ λΉ λ₯Έ μ¬λμ μκ² μ§λ§, GPUλ Colab μμ μλ€.

```python
import os

n_devices = torch.cuda.device_count()
print(n_devices)

for i in range(n_devices):
    print(torch.cuda.get_device_name(i))
```

`cuda.device_count()`κ° νμ¬ μ¬μ©νλ GPU κ°μμ’ μλ €λ¬λΌλ κ±΄λ°, μ κ² 0μ΄ λ¨λ©΄ GPUμμ°κ³  μλκ±°λ€. κ·ΈλκΉ. κΌ­ νμΈν΄λ³΄κ³  μλ¨λ©΄, μΌμͺ½ μλ¨μ λ°νμ -> λ°νμ νκ²½ λ³κ²½ -> GPUλ‘ λ³κ²½ν΄μ£Όμ.

```python
if torch.cuda.is_available():    
    device = torch.device("cuda")
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print('No GPU available, using the CPU instead.')
```

κ·Έλ λ€λ©΄, λ§μ§λ§μΌλ‘ GPU μ¬μ©κ°λ₯νμ§ μ²΄ν¬ν΄λ³΄κ³  GPUμ μ΄λ¦μ λ³Ό μ μλλ‘ μΈννμ.

```python
#BERT λͺ¨λΈ, Vocabulary λΆλ¬μ€κΈ°
bertmodel, vocab = get_pytorch_kobert_model()
```

λλμ΄ BERT λͺ¨νμ λΆλ¬μλ€. bertmodelμ λΆλ¬μ¨ λͺ¨λΈμ΄ μ μ₯, vocabλ μ¬μ©λλ νκ΅­μ΄ λ¨μ΄κ° μ μ₯ μ°Ύγμλ³΄λ vocabμλ 8000μ¬κ°μ νκ΅­μ΄ λ¨μ΄κ° λ€μ΄κ° μλ€κ³  νλ€. κ·Όλ° μ΄κ±° λ§€μ° μ μκ±°λ€. κ·Έλμ KoBERTμ νκ³μ μ΄λΌκ³ λ λΆλ¦°λ€.

κ·Έλ¦¬κ³  μ΄λλΆν° μ΄μ§ λΈλΌμ°μ μ λ°μμ΄ λ¦κ² μ¨λ€. (μκ°μ΄ κ±Έλ¦°λ€...γ )

```python
import pandas as pd
naturalTraining_data = pd.read_excel('.../αα‘α·αα₯αΌαα’ααͺαα‘α―αα?αΌαα΅(αα¬αα©αΌαα¦αα΅αα₯)_Training.xlsx')
```

κΈ°λ³Έμ μΌλ‘ λ°μ΄ν° νλ μνμμΌλ‘ λΆλ¬μ¨λ€.

μ΄μ  μ  μμ λ°μ΄ν°λ₯Ό μ¬μ©ν΄λ³΄κΈ° μν΄μλ λ°μ΄ν°μ μκΉμλ₯Ό νμΈν΄λ΄μΌνλ€. κ·Έλ¬κΈ° μν΄μλ μλμ κ°μ μ½λλ‘ μΌλΆλΆλ§ νμΈν  μ μλ€.

```python
naturalTraining_data.head()
naturalTraining_data.sample(n=10)
```

λ°μ΄ν°λ₯Ό μ μ²λ¦¬ ν ν λͺ¨λΈ νμ΅μ μν μΈνμ λ€μ΄κ°λ€.

```python
class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(
            bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)

        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))

    def __len__(self):
        return (len(self.labels))  
```

KoBERT λͺ¨λΈμ λ€μ΄κ° λ°μ΄ν° μμ λν classμ΄λ€.

```python
# Setting parameters νμ
max_len = 64
batch_size = 64
warmup_ratio = 0.1
num_epochs = 15
max_grad_norm = 1
log_interval = 100
learning_rate =  5e-5
```

μμ parameterλ₯Ό ν΅ν΄ μΈκ³΅μ§λ₯μ νμ΅μν΅λλ€.

```python
#ν ν°ν
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

data_train = BERTDataset(dataset_train, 0, 1, tok, max_len, True, False)
data_test = BERTDataset(dataset_test, 0, 1, tok, max_len, True, False)

train_dataloader = torch.utils.data.DataLoader(data_train, batch_size=batch_size, num_workers=5)
test_dataloader = torch.utils.data.DataLoader(data_test, batch_size=batch_size, num_workers=5)
```

```python
class BERTClassifier(nn.Module): ## ν΄λμ€λ₯Ό μμ
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=6,   ##ν΄λμ€ μ μ‘°μ ##
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)
```

ν΄λμ€ μ 6κ°λ₯Ό μ‘°μ νκ³  μ΄λ₯Ό ν΅ν΄ μΈκ³΅μ§λ₯μ black BoxμΈ hidden layerκΉμ§μ μΈνμ λͺ¨λ κ°μΆλ€.

```python

#BERT λͺ¨λΈ λΆλ¬μ€κΈ°
model = BERTClassifier(bertmodel,  dr_rate=0.5).to(device)
#optimizerμ schedule μ€μ 
no_decay = ['bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
    {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
]

optimizer = AdamW(optimizer_grouped_parameters, lr=learning_rate)
loss_fn = nn.CrossEntropyLoss()

t_total = len(train_dataloader) * num_epochs
warmup_step = int(t_total * warmup_ratio)

scheduler = get_cosine_schedule_with_warmup(optimizer, num_warmup_steps=warmup_step, num_training_steps=t_total)

#μ νλ μΈ‘μ μ μν ν¨μ μ μ
def calc_accuracy(X,Y):
    max_vals, max_indices = torch.max(X, 1)
    train_acc = (max_indices == Y).sum().data.cpu().numpy()/max_indices.size()[0]
    return train_acc
    
train_dataloader

for e in range(num_epochs):
    train_acc = 0.0
    test_acc = 0.0
    model.train()
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(tqdm_notebook(train_dataloader)):
        optimizer.zero_grad()
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length
        label = label.long().to(device)
        out = model(token_ids, valid_length, segment_ids)
        loss = loss_fn(out, label)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_grad_norm)
        optimizer.step()
        scheduler.step()  # Update learning rate schedule
        train_acc += calc_accuracy(out, label)
        if batch_id % log_interval == 0:
            print("epoch {} batch id {} loss {} train acc {}".format(e+1, batch_id+1, loss.data.cpu().numpy(), train_acc / (batch_id+1)))
    print("epoch {} train acc {}".format(e+1, train_acc / (batch_id+1)))
    
    model.eval()
    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(tqdm_notebook(test_dataloader)):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)
        valid_length= valid_length
        label = label.long().to(device)
        out = model(token_ids, valid_length, segment_ids)
        test_acc += calc_accuracy(out, label)
    print("epoch {} test acc {}".format(e+1, test_acc / (batch_id+1)))
```

νμ΅ μ§ν

```python
## νμ΅ λͺ¨λΈ μ μ₯
PATH = 'drive/MyDrive/colab/StoryFlower/bert' # google λλΌμ΄λΈ μ°λ ν΄μΌν¨. κ΄λ ¨μ½λλ λΊμ
torch.save(model, PATH + 'KoBERT_λ΄ν.pt')  # μ μ²΄ λͺ¨λΈ μ μ₯
torch.save(model.state_dict(), PATH + 'model_state_dict.pt')  # λͺ¨λΈ κ°μ²΄μ state_dict μ μ₯
torch.save({
    'model': model.state_dict(),
    'optimizer': optimizer.state_dict()
}, PATH + 'all.tar')  # μ¬λ¬ κ°μ§ κ° μ μ₯, νμ΅ μ€ μ§ν μν© μ μ₯μ μν΄ epoch, loss κ° λ± μΌλ° scalarκ° μ μ₯ κ°λ₯
```

λͺ¨λΈμ μ μ₯ν μ΄ν νμ΅ν λͺ¨λΈμ λΆλ¬μ μ¬μ©ν΄μΌν  μ½λλ λ€μκ³Ό κ°λ€.

```python
!pip install mxnet
!pip install gluonnlp pandas tqdm
!pip install sentencepiece
!pip install transformers==3.0.2
!pip install torch

!pip install git+https://git@github.com/SKTBrain/KoBERT.git@master

# torch
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook

#kobert
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

#GPU μ¬μ©
device = torch.device("cuda:0")

#BERT λͺ¨λΈ, Vocabulary λΆλ¬μ€κΈ° νμ
bertmodel, vocab = get_pytorch_kobert_model()


# KoBERTμ μλ ₯λ  λ°μ΄ν°μ μ λ¦¬
class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(
            bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)

        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))

    def __len__(self):
        return (len(self.labels))  

# λͺ¨λΈ μ μ
class BERTClassifier(nn.Module): ## ν΄λμ€λ₯Ό μμ
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=6,   ##ν΄λμ€ μ μ‘°μ ##
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)

# Setting parameters
max_len = 64
batch_size = 32
warmup_ratio = 0.1
num_epochs = 20
max_grad_norm = 1
log_interval = 100
learning_rate =  5e-5

## νμ΅ λͺ¨λΈ λ‘λ
PATH = 'drive/MyDrive/colab/StoryFlower/bert/'
model = torch.load(PATH + 'KoBERT_λ΄ν_86.pt')  # μ μ²΄ λͺ¨λΈμ ν΅μ§Έλ‘ λΆλ¬μ΄, ν΄λμ€ μ μΈ νμ
model.load_state_dict(torch.load(PATH + 'model_state_dict_86.pt'))  # state_dictλ₯Ό λΆλ¬ μ¨ ν, λͺ¨λΈμ μ μ₯

#ν ν°ν
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

def new_softmax(a) : 
    c = np.max(a) # μ΅λκ°
    exp_a = np.exp(a-c) # κ°κ°μ μμμ μ΅λκ°μ λΊ κ°μ expλ₯Ό μ·¨νλ€. (μ΄λ₯Ό ν΅ν΄ overflow λ°©μ§)
    sum_exp_a = np.sum(exp_a)
    y = (exp_a / sum_exp_a) * 100
    return np.round(y, 3)


# μμΈ‘ λͺ¨λΈ μ€μ 
def predict(predict_sentence):

    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=5)
    
    model.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length= valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids)

        test_eval=[]
        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()
            min_v = min(logits)
            total = 0
            probability = []
            logits = np.round(new_softmax(logits), 3).tolist()
            for logit in logits:
                print(logit)
                probability.append(np.round(logit, 3))

            if np.argmax(logits) == 0:  emotion = "κΈ°μ¨"
            elif np.argmax(logits) == 1: emotion = "λΆμ"
            elif np.argmax(logits) == 2: emotion = 'λΉν©'
            elif np.argmax(logits) == 3: emotion = 'μ¬ν'
            elif np.argmax(logits) == 4: emotion = 'λΆλΈ'
            elif np.argmax(logits) == 5: emotion = 'μμ²'

            probability.append(emotion)
            print(probability)
    return probability
```

μ΄μ  μ μ½λλ₯Ό django μλ²μ λ°μνλ©΄ λλ€.

νΉν νμ΅ν λͺ¨λΈμ djangoμ λ‘λν  λ νμν ν΄λμ€μΈ `BERTDataset`μ `BERTClassifier`μ `manage.py`μ μΈνν λ€μ λͺ¨λΈμ `Apps.py`μμ λ‘λνμ.

## π KNN μΆμ² μκ³ λ¦¬μ¦

- μ ν΄λ¦¬λμ κ±°λ¦¬ κ³΅μμ μ΄μ©ν μ μ¬ κ°μ  κ½ μΆμ²

- λ§€μ° κ°λ¨ν μκ³ λ¦¬μ¦μ΄λ©°, μ½λ μ°μ°μ ν° μ΄λ €μμ΄ μκΈ° λλ¬Έμ μμΈν λΆλΆμ μλ΅νλ€.

  **Why KNN ?**

  - KoBERT λͺ¨λΈμ νμ€νΈλ₯Ό λμ ν λμ€λ κ²°κ³Όλ¬Όμ νλμ λ¨μ΄κ° μλ νΉμ μ κ°μ μ μν  κ°μ€μΉ κ°μ΄λ€. κ·Έ κ°μ΄ ν΄μλ‘ ν΄λΉ κ°μ μΌ νλ₯ μ΄ λμμ μλ―Ένλ€. μ΄λ λ³Έ νλ‘μ νΈμμ μ£Όμν΄μΌν  λΆλΆμ΄κΈ°λ νλ€. ν μ¬λμ΄ μλ ₯ν νμ€νΈ μμλ νλμ κ°μ λ§ λ΄κ²¨μμ§ μλ€. λ°λΌμ 6κ°μ κ°μ  λλΆλ₯λ₯Ό λͺ¨λ κ²μ¬νμ¬ κ½λ§ + κ½μ λ°°κ²½μΌλ‘ μΈν΄ λ±μ₯ν νλ₯ κ°κ³Ό μ¬μ©μκ° μλ ₯ν νμ€νΈλ‘ μΈν΄ λ±μ₯ν νλ₯ κ° μ¬μ΄μ κ°μ₯ μ΅μμ κ±°λ¦¬λ₯Ό μ§λ κ½μ μΆμ²νλ κ²μ΄ λͺ¨λ  κ°μ μ κ³ λ €νμ¬ μ¬μ©μμκ² κ½μ μΆμ²νλ λ§₯λ½μ μ΄μΈλ¦¬κΈ° λλ¬Έμ μ€μλ₯Ό μΉμ­μΌλ‘ ν κ°μ€μΉ κ°μ softmaxν¨μλ₯Ό μ¬μ©νμ¬ νμ€νΈλ₯Ό νλ₯ κ°μΌλ‘ λ³ννκ³  μ΄λ₯Ό ν΅ν΄ κ½μ μΆμ²νλ KNN μκ³ λ¦¬μ¦μ μ¬μ©νκ² λμλ€.

``` python
# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
import numpy as np
import pandas as pd
import sys
from os import path
# Message Recommend
@api_view(['POST', 'GET'])
def msg_recomm(request):
    if request.method == 'POST':
        print("Django Success!")
        data = request.data.get('msg') # Spring μμ²­ λ°μ΄ν°
        print("request data : " + data)

        # KoBert κ°μ  λΆμ λͺ¨λΈ
        # model_result = [21.45123, 10.1234, 4.012312, 4.01234, 31.43234, 13.123415]
        sys.path.append(path.join(path.dirname(__file__), '..'))
        from kobert_predict import predict
        model_result = predict(data)

        # knn μκ³ λ¦¬μ¦
        flag = True
        datas = knn(model_result, flag)
        print (datas)

        return Response(data=datas, status=status.HTTP_200_OK)

# State Recommend
@api_view(['POST'])
def state_recomm(request):
    if request.method == 'POST':
        print("Django Success!")
        data = request.data.get('state') # Request data
        print("request data : " + data)

        # KoBert κ°μ  λΆμ λͺ¨λΈ load
        sys.path.append(path.join(path.dirname(__file__), '..'))
        from kobert_predict import predict
        model_result = predict(data)
        state = model_result[6]

        # knn μκ³ λ¦¬μ¦
        flag = False
        datas = knn(model_result, flag)
        response = {
            'fno': datas,
            'state' : state
        }
        print(datas)

        return Response(data=response, status=status.HTTP_200_OK)

def knn(model_result, flag):
    # DB emotion μ‘°ν
    try:
        cursor = connection.cursor()
        strSql = "SELECT fno, happy, unstable, embarrass, sad, angry, hurt FROM emotion"
        result = cursor.execute(strSql)
        emotion = cursor.fetchall()

        connection.commit()
        connection.close()

        datas = []
        for data in emotion:
            # DB νλ₯ κ°λ§ μ μ₯
            tmp = [data[1], data[2], data[3], data[4], data[5], data[6]]

            # μ ν΄λ¦¬λμ distance
            sum = 0
            for i in range(0, len(tmp)):
                df = model_result[i] - tmp[i]  # λ°°μ΄κ° λΊμ
                df = df ** 2  # λ°μ΄ν°μ μ κ³±
                sum += df

            row = {
                'fno': data[0],  # flower primary key
                'distance': np.sqrt(sum)  # λ°μ΄ν°λ€μ ν©μ μ κ³±κ·Ό = κ±°λ¦¬
            }

            datas.append(row)

        df1 = pd.DataFrame(datas,columns=['fno','distance']) # κ²°κ³Ό dataframe μμ±
        df1 = df1.sort_values('distance').head(5) # distanceκ° κ°μ₯ μμ μμΌλ‘ μ λ ¬ ν μμ 5κ° μΆμΆ
        print(df1)

        # μμ 5κ° fno listλ‘ μΆμΆ
        result_fno = []
        for index, row in df1.iterrows():
            result_fno.append(int(row['fno']))

        if(flag):
            return result_fno
        else:
            return result_fno[0]
    except:
        connection.rollback()
        print("Failed selecting in emotion")
```

djangoμ λ°μλ μ½λλ μμ κ°λ€.