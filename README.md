# Modelo-Machine-Learning-N-o-Aprendizado-SupervisionadoMarcelo, com base no código enviado, trata-se de um projeto de **Machine Learning Não Supervisionado** utilizando o algoritmo **K-Means Clustering** para identificação de grupos (clusters) em dados sem rótulos. O projeto utiliza conceitos fundamentais apresentados no livro *Data Science para Negócios* de Foster Provost e Tom Fawcett, especialmente sobre descoberta de padrões, segmentação e aprendizado não supervisionado. 

Você pode utilizar o seguinte conteúdo no arquivo **README.md** do GitHub:

---

# Projeto de Machine Learning Não Supervisionado com K-Means

## 📌 Sobre o Projeto

Este projeto demonstra a aplicação de técnicas de **Aprendizado de Máquina Não Supervisionado (Unsupervised Learning)** utilizando o algoritmo **K-Means Clustering**.

O objetivo é identificar agrupamentos naturais em um conjunto de dados sem a necessidade de variáveis-alvo previamente definidas, permitindo a descoberta de padrões ocultos e segmentações relevantes.

A abordagem está fundamentada nos conceitos apresentados no livro:

📖 **Data Science para Negócios** – Foster Provost e Tom Fawcett

---

## 🎯 Objetivos

* Aplicar técnicas de clusterização.
* Identificar grupos semelhantes dentro dos dados.
* Demonstrar o funcionamento do algoritmo K-Means.
* Realizar pré-processamento dos dados.
* Visualizar clusters e centroides gerados pelo modelo.

---

## 🛠 Tecnologias Utilizadas

### Linguagem

* Python 3.x

### Bibliotecas

#### NumPy

Utilizada para manipulação numérica e geração de dados aleatórios.

```python
import numpy as np
```

#### Matplotlib

Responsável pela visualização gráfica dos clusters e centroides.

```python
import matplotlib.pyplot as plt
```

#### Scikit-Learn

Biblioteca principal de Machine Learning utilizada no projeto.

Componentes utilizados:

* KMeans
* make_blobs
* StandardScaler

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
```

---

##  Fluxo do Projeto

### 1. Geração dos Dados

São criados dados sintéticos utilizando a função `make_blobs()`, simulando diferentes grupos de observações.

### 2. Normalização

Os dados são padronizados utilizando `StandardScaler`, garantindo que todas as variáveis possuam a mesma escala.

### 3. Treinamento do Modelo

O algoritmo K-Means é treinado para identificar automaticamente os agrupamentos existentes nos dados.

### 4. Definição dos Centroides

Após o treinamento, o modelo calcula os centroides que representam o centro de cada cluster.

### 5. Visualização

Os resultados são exibidos graficamente, destacando:

* Clusters encontrados
* Centroides
* Distribuição dos dados

### 6. Métricas

O modelo apresenta:

* Número de clusters
* Inércia (Inertia)
* Número de iterações realizadas

---

##  Conceitos de Data Science Aplicados

Este projeto aborda conceitos fundamentais de Data Science para Negócios:

* Descoberta de conhecimento em dados (KDD)
* Segmentação de clientes
* Agrupamento de padrões
* Análise exploratória de dados
* Aprendizado não supervisionado
* Clusterização
* Preparação e normalização de dados

---

## 🚀 Possíveis Aplicações de Negócio

* Segmentação de clientes
* Agrupamento de produtos
* Análise de comportamento de consumidores
* Detecção de padrões de compra
* Agrupamento geográfico
* Análise de perfis de usuários
* Estratégias de marketing direcionado

---

## 📖 Referência Bibliográfica

**Provost, Foster; Fawcett, Tom.**

*Data Science para Negócios: O que você precisa saber sobre mineração de dados e pensamento analítico de dados.*

Editora Alta Books.

---

## 👨‍💻 Autor

**Marcelo Rodrigues**
Consultor de Dados | Business Intelligence | Machine Learning
**Starts BI**

---


