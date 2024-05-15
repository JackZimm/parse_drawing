# parse_drawing
This code is written to help a company do a drawing based on the comments on social media posts. 

The data set starts with * Reply, followed by the original user's name, and then followed by their comment, which will contain the contestants. There is no need for the reply or the original user's name in the list, as they cannot win the drawing, but only the names that follow. This code will skip over the reply keyword and the first value that follows it, only adding the contestants to the final drawing. 
This code is also set to take either a dictionary or a list as an argument, and will not work if used with any other type of data set, such as a tuple or such. 
