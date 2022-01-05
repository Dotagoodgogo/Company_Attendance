import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import Image
import time
import multiprocessing.dummy
from Backend import Database

class face():
    def __init__(self):
        self.I = Database()
        self.list = self.I.fetchcode()
        self.ID = self.I.fetchID() + 1
        self.videolist=[]

    def videocapture(self):
        x = 0
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        y = 0
        name = f'Video/{x}.avi'
        self.videolist.append(name)
        out = cv2.VideoWriter(name, fourcc, 20, (640, 480))
        while (cap.isOpened()):
            ret, img = cap.read()
            if ret == True:
                out.write(img)
                y += 1
                if y == 90:
                    x += 1
                    out.release()
                    name = f'Video/{x}.avi'
                    self.videolist.append(name)
                    out = cv2.VideoWriter(name, fourcc, 20, (640, 480))
                    #out.write(img)
                    y = 0

                # cv2.imshow("Frame",img)

                key = cv2.waitKey(1)
                if key == ord('n') or key == ord('q'):
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def Facetec(self):
        self.videolist=['0.avi','1.avi','2.avi','3.avi','4.avi','5.avi']
        path="Video"
        #self.deletefile()
        while True:
            if len(self.videolist) == 0:
                continue
            del self.videolist[-1]
            for i in self.videolist:
                video = cv2.VideoCapture(i)
                while True:

                    success, img = video.read()

                    if success == True:
                        imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)    #缩小处理画框加快处理速度
                        imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
                        faceLoc = face_recognition.face_locations(imgs)     #定位人脸位置
                        encode = face_recognition.face_encodings(imgs, faceLoc, num_jitters=1) #给所有脸部编码
                        for encodeface, face in zip(encode, faceLoc):
                            if self.confirm(encodeface) == False:
                                self.list.append(encodeface)
                                Bytes = encodeface.dumps()
                                a, b, c, d, = face
                                face_img = img[4 * a:4 * c, 4 * d:4 * b]
                                face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

                                pil_image = Image.fromarray(face_img)
                                pil_image.save(f'Photo/{os.path.splitext(i)[0]}_{self.ID}.jpg')#照片名为照片ID和人脸ID
                                blob_value = open(f'Photo/{os.path.splitext(i)[0]}_{self.ID}.jpg', 'rb').read()
                                self.I.insert(blob_value, Bytes)

                        for encodeface, faceloca in zip(encode, faceLoc):
                            self.FindName(encodeface)

                    else:
                        break

                    cv2.imshow("niubi!", img)
                    cv2.waitKey(1)

                video.release()
                cv2.destroyAllWindows()
                os.remove(f"{path}/{i}")
                self.videolist.remove(i)


    def confirm(self,CAMFacecode):
        result = face_recognition.compare_faces(self.list, CAMFacecode,tolerance=0.6)

        if True in result:
            return True
        for i in range(3):
            result = face_recognition.compare_faces(self.list, CAMFacecode,tolerance=0.6)
            if True in result:
                return True
        return False

    def deletefile(self):
        dir = 'Video'
        dir2 = 'Photo'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        for f in os.listdir(dir2):
            os.remove(os.path.join(dir2, f))


    def FindName(self,x):
        faceDistance = face_recognition.face_distance(self.list, x)
        matchindex = np.argmin(faceDistance)
        self.matchname = self.I.FindName(self.list[matchindex].dumps())
        print(self.matchname)
        if self.matchname == None:
            self.matchname="Unknown"

'''
    def rectangleandmark(self,img,faceloca):
        cv2.rectangle(img, (4 * faceloca[3], 4 * faceloca[0]), (4 * faceloca[1], 4 * faceloca[2]), (0, 255, 0), 2)
        #cv2.rectangle(img, (4 * faceloca[3], 4 * faceloca[2]-35), (4 * faceloca[1],4*faceloca[2]), (0, 255, 0), cv2.FILLED)  # 画正方形在原图下方，填充颜色
        cv2.putText(img,self.matchname, (4 * faceloca[3], 4 * faceloca[0]-20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
'''



'''
if __name__ == "__main__":
    p = face()
    process1 = []

    p1 = multiprocessing.dummy.Process(target=p.videocapture)
    p1.start()
    process1.append(p1)

    p2 = multiprocessing.dummy.Process(target=p.Facetec)
    p2.start()
    process1.append(p2)

    for i in process1:
        i.join()
'''





p=face()
#p.videocapture()
#p.deletefile()
p.Facetec()
