import statistics
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
journal = {'Aaron':grades[0],'Bilbo':grades[1], 'Johnny':grades[2], 'Khendrik':grades[3], 'Steve':grades[4]}
average_1 = sum(journal['Aaron'])/len(journal['Aaron'])
average_2 = sum(journal['Bilbo'])/len(journal['Bilbo'])
average_3 = sum(journal['Johnny'])/len(journal['Johnny'])
average_4 = sum(journal['Khendrik'])/len(journal['Khendrik'])
average_5 = sum(journal['Steve'])/len(journal['Steve'])
results = {'Aaron':average_1,'Bilbo':average_2,'Johnny':average_3,'Khendrik':average_4,'Steve':average_5}
print(results)

average_1_2 = statistics.mean(journal['Aaron'])
average_2_2 = statistics.mean(journal['Bilbo'])
average_3_2 = statistics.mean(journal['Johnny'])
average_4_2 = statistics.mean(journal['Khendrik'])
average_5_2 = statistics.mean(journal['Steve'])
results_2 = {'Aaron':average_1_2,'Bilbo':average_2_2,'Johnny':average_3_2,'Khendrik':average_4_2,'Steve':average_5_2}
print(results_2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
