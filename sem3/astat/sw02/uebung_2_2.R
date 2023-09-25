marks <- c(4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1)

sorted_marks <- sort(marks)
sorted_marks

median(sorted_marks)
mean(sorted_marks)

sorted_marks[9] = 1
sorted_marks[10] = 1
sorted_marks[11] = 1

median(sorted_marks)
mean(sorted_marks)

boxplot(marks, sorted_marks,col = c("orange", "lightblue"))

