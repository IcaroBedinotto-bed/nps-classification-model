# 📊 NPS Classification Model

Projeto de Machine Learning para classificação de clientes em **Promoters, Passives e Detractors**, com foco em entender e permitir que os times envolvidos na operação e CS atuem de maneira proativa para reduzir o volume de detratores

---

## 🚀 Objetivo

Desenvolver um modelo capaz de prever quando um dado usuário será detrator, permitindo:

* Antecipar clientes insatisfeitos (detratores)
* Identificar oportunidades de melhoria na jornada
* Apoiar decisões de negócio orientadas a dados

---

## 🧠 Contexto do Problema

A empresa em questão atua no e-commerce e por conta do forte crescimento da demanda tem visto os indicadores de satisfação do cliente despencarem. Em um dataset com 2.500 registros **+80% dos clientes foram classificados como detratores (NPS < 7)**.

Esse aumento de detratores impactou diretamente na retenção de clientes, logo a empresa tem que atuar de maneira proativa para reduzir fricções na jornada.

Verificou-se que o principal ofensor de experiência é o atraso médio do pedido

## Descrição da base de dados

Base de dados com 2.500 registros, sendo dados de identificação do usuário e do pedido, bem como informações do pedido, dados operacionas e NPS e CSAT que definem a satisfação.

Base de dados pode ser acessada em src > data > desafio_nps.csv

Abaixo está o dicionário de dados

* customer_id: Identificador único do cliente. 
* order_id: Identificador único do pedido. 
* customer_age: Idade do cliente. 
* customer_region: Região geográfica do cliente. 
* customer_tenure_months: Tempo de relacionamento do cliente com a 
empresa (em meses). 
* order_value: Valor total do pedido. 
* items_quantity: Quantidade de itens no pedido. 
* discount_value: Valor de desconto aplicado ao pedido. 
* payment_installments: Número de parcelas do pagamento. 
* delivery_time_days: Tempo total de entrega (em dias). 
* delivery_delay_days: Quantidade de dias de atraso na entrega. 
* freight_value: Valor do frete. 
* delivery_attempts: Número de tentativas de entrega. 
* customer_service_contacts: Número de contatos do cliente com o 
atendimento. 
* resolution_time_days: Tempo para resolução de problemas (em dias). 
* complaints_count: Número de reclamações registradas pelo cliente. 
* repeat_purchase_30d: Indica se houve recompra em até 30 dias após o 
pedido (0 = não, 1 = sim). 
* csat_internal_score: Score interno de satisfação do cliente. 
* nps_score: Nota de satisfação do cliente (NPS), variando de 0 a 10, coletada 
após a experiência de compra. 



---

## 🗂️ Estrutura do Projeto

```
.
├── data/
│   ├── raw/              # Dados brutos
│   └── processed/        # Dados tratados
│
├── src/
│   ├── data/             # Leitura e tratamento de dados
│   ├── features/         # Feature engineering
│   ├── models/           # Treinamento e avaliação
│   │   ├── train_model.py
│   │   ├── evaluate_model.py
│   │   └── model_factory.py
│   └── utils/
│
├── main.py               # Pipeline principal
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* pandas
* scikit-learn
* imbalanced-learn (SMOTE)

---

## 📊 Features Utilizadas (Input)

* customer_age
* customer_tenure_months
* order_value
* items_quantity
* discount_value
* payment_installments
* delivery_time_days
* delivery_delay_days
* freight_value
* delivery_attempts
* customer_service_contacts
* resolution_time_days
* complaints_count
* csat_internal_score

---

## 🔄 Pipeline do Modelo

1. **Leitura dos dados**
2. **Feature engineering**: Classificação dos pedidos seguindo a metodologia do NPS
3. **Separação entre treino e teste**: 30% para treinamento e 70% para teste
4. **Tratamento de desbalanceamento**: Forçamos o balanceamento dos dados e aplicamos o Random Forest dada as características dos dados
5. **Treinamento do modelo**
6. **Avaliação por métricas de classificação**:
   - 

---

## 🤖 Modelos Testados

* Logistic Regression
* Random Forest

Ambos os modelos foram avaliados com e sem:

* balanceamento de classes
* técnicas de oversampling

---

## 📈 Resultados (Baseline)

### Random Forest (sem tratamento de desbalanceamento)

| Classe    | Precision | Recall | F1-score |
| --------- | --------- | ------ | -------- |
| Promoter  | 0.50      | 0.06   | 0.11     |
| Passive   | 0.12      | 0.01   | 0.02     |
| Detractor | 0.84      | 0.99   | 0.91     |

**Acurácia:** 0.83

Dado que o ojetivo é garantir assertividade no diagnóstico de detratores, usamos como base o Recall

---

## ⚠️ Limitações

* Dataset altamente desbalanceado
* Baixa representatividade de Promoters e Passives
* Modelos iniciais com baixa capacidade de generalização para classes minoritárias, logo priorizamos em identificar detratores

---

## ▶️ Como Executar

1. Clone o repositório:

```
git clone <[url-do-repositorio](https://github.com/IcaroBedinotto-bed/tech-challegenge-grupo-47)>
```

2. Crie um ambiente virtual:

```
python -m venv venv
```

3. Ative o ambiente:

* Windows:

```
venv\Scripts\activate
```

* Linux/Mac:

```
source venv/bin/activate
```

4. Instale as dependências:

```
pip install -r requirements.txt
```

5. Execute o pipeline:

```
python main.py
```

---
