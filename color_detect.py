# Importing Libraries
import pandas as pd
import cv2

# Function for RGB Values
def get_color_name(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R-int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B-int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            color_name = df.loc[i, 'color_name']
    return color_name

# Function for Mouse Click Event
def draw_function(event, x, y, flags, params):
    global clicked, r, g, b, xpos, ypos
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked, xpos, ypos = True, x, y
        b, g, r = list(map(int, img[y, x]))


# Assigning Path
img_path = r"C:\Users\Siddharth\PycharmProjects\color-identification-opencv-master\imgs\img5.jpg"
csv_path = r"C:\Users\Siddharth\PycharmProjects\color-identification-opencv-master\colors.csv"
img = cv2.imread(img_path)
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# Creating the dataframe for colors csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

# Window to display the image
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_function)
clicked, r, g, b, xpos, ypos = False, 0, 0, 0, 0, 0

# On click action
while True:
    cv2.imshow("Image", img)
    if clicked:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness=-1) {-1 = fills entire rectangle }
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)

        # Text for display information
        text = get_color_name(r, g, b) + ' R:' + str(r) + ' G:' + str(g) + ' B:' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        #  For very light color show the text in black color
        if r+g+b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
