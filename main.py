import matplotlib.pyplot as plt
import streamlit as st
import csv

def get_empty_data(lines, index):
    miss = 0
    total = len(lines)
    share = 0
    for line in lines:
        lst = line.strip().split(',')
        if lst[index] == '':
            miss += 1
            share = miss / total * 100
    return miss, share

st.image('30-1-1204x483.jpg')
columns = ['PassengerId',	'Survived',	'Pclass',	'Name', 'Sex',	'Age',	'SibSp', 'Parch',	'Ticket',	'Fare',	'Cabin',	'Embarked']
st.title('Отсутствие данных о пассажирах')
st.write('Для просмотра информации о количестве пассажиров, по которым нет данных, выберите соответствующую категорию')
choice = st.selectbox('Выберите категорию:', columns)
index = columns.index(choice)

if index > 3:
    index += 1

with open('data.csv') as file:
    lines = file.readlines()[1:]

miss, share = get_empty_data(lines, index)
data = {'Категория':['Количество пассажиров без данных', 'Доля,%'], 'Данные': [miss, share]}
st.table(data)


fig = plt.figure(figsize=(10, 5))
plt.bar(choice, miss)
plt.xlabel("Наименование категории")
plt.ylabel("Количество пассажиров")
plt.title("Количество пассажиров, по которым отсутствуют данные")
st.pyplot(fig)

