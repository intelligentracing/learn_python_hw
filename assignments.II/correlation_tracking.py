import numpy as np
import cv2
import os
#状态
LOST_TRACK = 0
UPDATE_TRACK = 1
#读取文件
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/jump_rope.mp4'
XMLAddress = path+'/haarcascade_frontalface_alt.xml'
#滤波函数
face_cascade = cv2.CascadeClassifier(XMLAddress) 
#读取文件
grabber = cv2.VideoCapture(filename) 
#将长宽减少一半
width = int(grabber.get(cv2.CAP_PROP_FRAME_WIDTH))//2
height = int(grabber.get(cv2.CAP_PROP_FRAME_HEIGHT))//2
#保存设置为True
save_result = True
#如果保存
if save_result:
    #输出名称设置为result
    output_filename = path + '\result.avi'
    #读取帧率
    fps = int(grabber.get(cv2.CAP_PROP_FPS))
    #外放写入
    output = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc('M', 'J', 'P','G'),\
        fps, (width, height), True)
#设置追踪状态
trackingStatus = LOST_TRACK
#当可以读取每一帧
while (grabber.isOpened()): 
    #设置第一项为返回值,接受第二项数据
    return_flag, frame = grabber.read()  
    #如果接受失败
    if not(return_flag):
        #循环中断
        break
    #将图片压缩
    frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_CUBIC)
    #如果追踪失败
    if trackingStatus == LOST_TRACK:
        #转化为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        #检测面部图像
        faces = face_cascade.detectMultiScale(gray, 1.1, 10)
        #如果监测到面部图像
        if len(faces)>0:
            #筛选最大图像
            largestArea = 0
            for i in range(len(faces)):
                if faces[i][2]*faces[i][3] > largestArea:
                    largestArea = faces[i][2]*faces[i][3]
                    largestFace = faces[i]
            #初始化追踪器
            # Possible choices in cv2:
            # TrackerBoosting, TrackerMIL, TrackerKCF, TrackerTLD, TrackerMOSSE, TrackerCSRT
            tracker = cv2.TrackerKCF_create()
            x = max(largestFace[0]-largestFace[2]//2 , 0)
            y = max(largestFace[1]-largestFace[3]//2, 0)
            w = (largestFace[0]-x)*2 + largestFace[2]
            h = (largestFace[1]-y)*2 + largestFace[3]
            status = tracker.init(frame, (x,y, w, h))
            #如果监测初始化成功
            if status:
                #将状态设置为更新
                trackingStatus = UPDATE_TRACK
    # 若状态为更新
    else:
        #获取更新后的状态
        status, boundingBox = tracker.update(frame)
        #如果获取成功
        if status:
            #h画出更新后人脸的位置
            x, y, w, h = boundingBox
            x = int(x); y = int(y); w = int(w); h = int(h)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            #如果更新失败
        else:
            #监测状态设置为丢失
            trackingStatus = LOST_TRACK
            #打印
            print('Lost Track!')
    #展示视频
    cv2.imshow('Video',frame)
    #如果保存数据
    if save_result:
        #保存数据
        output.write(frame)
    #等待输入
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
#释放grabber
grabber.release()
#如果保存结果
if save_result:
    #保存
    output.release()
    #删除所有窗口
cv2.destroyAllWindows()
