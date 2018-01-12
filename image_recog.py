from numpy import ones,vstack
from numpy.linalg import lstsq
from statistics import mean
from config import *

def find_main_lanes(img, lines, color=[0, 255, 255], thickness=3):

    # if this fails, go with some default line
    try:
        # finds the maximum y value for a lane marker 
        # (since we cannot assume the horizon will always be at the same point.)

        ys = []
        for i in lines:
            for ii in i:
                ys += [ii[1],ii[3]]
        #print(lines)
        min_y = min(ys)
        max_y = 200
        #mid_y = 150
        new_lines = []
        line_dict = {}

        for idx,i in enumerate(lines):
            for xyxy in i:
                # These four lines:
                # modified from http://stackoverflow.com/questions/21565994/method-to-return-the-equation-of-a-straight-line-given-two-points
                # Used to calculate the definition of a line, given two sets of coords.
                x_coords = (xyxy[0],xyxy[2])
                y_coords = (xyxy[1],xyxy[3])
                A = vstack([x_coords,ones(len(x_coords))]).T
                m, b = lstsq(A, y_coords)[0]
                #print('m,b=',m,b)
                if m==0:
                    m=1
                # Calculating our new, and improved, xs
                x1 = (min_y-b) / m
                x2 = (max_y-b) / m
                #mid_x = (mid_y-b)/m
                #print('x1,x2=',x1,x2)

                line_dict[idx] = [m,b,[int(x1), min_y, int(x2), max_y]]
                new_lines.append([int(x1), min_y, int(x2), max_y])

        final_lanes = {}

        for idx in line_dict:
            final_lanes_copy = final_lanes.copy()
            m = line_dict[idx][0]
            b = line_dict[idx][1]
            line = line_dict[idx][2]
            
            if len(final_lanes) == 0:
                final_lanes[m] = [ [m,b,line] ]
                
            else:
                found_copy = False

                for other_ms in final_lanes_copy:
                    if not found_copy:
                        if abs(other_ms*1.2) > abs(m) > abs(other_ms*0.8):
                            if abs(final_lanes_copy[other_ms][0][1]*1.2) > abs(b) > abs(final_lanes_copy[other_ms][0][1]*0.8):
                                final_lanes[other_ms].append([m,b,line])
                                found_copy = True
                                break
                        else:
                            final_lanes[m] = [ [m,b,line] ]

        line_counter = {}

        for lanes in final_lanes:
            line_counter[lanes] = len(final_lanes[lanes])

        top_lanes = sorted(line_counter.items(), key=lambda item: item[1])[::-1][:2]

        lane1_id = top_lanes[0][0]
        lane2_id = top_lanes[1][0]

        def average_lane(lane_data):
            x1s = []
            y1s = []
            x2s = []
            y2s = []
            for data in lane_data:
                x1s.append(data[2][0])
                y1s.append(data[2][1])
                x2s.append(data[2][2])
                y2s.append(data[2][3])
            return int(mean(x1s)), int(mean(y1s)), int(mean(x2s)), int(mean(y2s))

        l1_x1, l1_y1, l1_x2, l1_y2 = average_lane(final_lanes[lane1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = average_lane(final_lanes[lane2_id])

        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2]
    except Exception as e:
        print(str(e))

# line detection
def detect_edge(rgb_image):
    #gray_img = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)   
    processed_img = cv2.Canny(rgb_image, threshold1=200, threshold2=300)
    #processed_img = cv2.Canny(gray_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (3,3), 0 )    
    
    vertices = np.array([[0,200],[0,0],[800,0],[800,200]], np.int32)
    #processed_img = roi(processed_img, [vertices])
    #plt.imshow(processed_img)    
    
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 120, 20, 35)
    print(lines)
    #draw_lines(processed_img,lines)    
    return processed_img, lines




# 找出黄线
def find_yellow_lane_BGR(org_img):
    """This function is to find the possible lines in yellow, and return them
    in form: [[x1,y1,x2,y2],
              [x1,y1,x2,y2],
              [x1,y1,x2,y2],
              ...
              ]
    """
    res_yellow=extract_with_yellowBGR(org_img)
    yellow_edge_img,yellow_edge_lines = detect_edge(res_yellow)
    return yellow_edge_lines

# 确定两条直线的相对距离（在y=y_max处的距离），以做参考
def distance(l1,l2):
    """ distance calculate the distance of two line at y=y_max, actually it is the distance between two points
    actually it is not the perpenticular distance between two lines.
    distance = x2 - x1:
    # if x2 - x1 > 0: then line 2 is on the right side of line 1
    # if x2 - x1 < 0: then line 2 is on the left side of line 1
    """ 
    m1 = l1[0]
    m2 = l2[0]
    b1 = l1[1]
    b2 = l2[1]
    max_y = HEIGHT
    x1 = (max_y-b) / m1
    x2 = (max_y-b) / m2 ## max_y这个地方要用height
    return x2-x1
