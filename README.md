项目标题：人脸识别自动签到系统
项目背景：2021年七月在张家港金典软件实习中的项目
项目功能：公司原本使用传统打卡方式，这个项目的目的是采用python的人脸识别库比如是facerecognation和opencv来测试这一个想法。利用摄像头采取人脸将数据库中的员工人脸与摄像头中的人脸进行比较。
项目复盘和思考：python库中的opencv和facerecognation库是人脸识别入门相对好用的库，但是对于应用上来还是欠佳。在测试程序的时候，我发现因为要经过每一帧视频进行大量计算。导致视频运行起来非常卡顿。非常难正常运行。接下来我计划将视频自动保存为视频，然后充分利用cpu进行多进程处理，但是效果还是欠佳。结果导致在实习结束前没有完成项目。同时，因为没有团队，缺少交流。所以导致项目发展缓慢。

人脸识别（V2）：
要求：
输入：用Face Recognation输入视频
处理：
进程1：保存视频
进程2：收取保存视频然后做人脸识别过程
存入数据库
与数据库中数据作比较
数据库:
创建数据库：
表格属性（5个）：姓名(VARCHAR(50))，图片（BLOB），编码（BLOB），人脸号（int PRIMARY KEY AUTO_INCREMENT），时间 (VARCHAR(50))

收集数据：
函数1（参数：图片，编码）-->读入未有人脸图片和编码
主体
无return值
函数2（无参数）-->调出所有人脸
主体
return 列表编码值

函数3（无参数）-->调取整个相应人脸ID
主体
return 对应人脸ID
函数4：（无参数）导入对应时间（时间）：
主体
无return值

函数5：（无参数）清空时间数据
主体
无return值


Project Title: Face Recognition Automatic Sign-in System
Project background: July 2021 in Zhangjiagang Jindian software internship project
Project Function: The company originally used the traditional punch card method, the purpose of this project is to use python face recognition libraries such as facerecognation and opencv to test this one idea. Use the camera to take the face to compare the employee's face in the database with the face in the camera.
Project review and reflection: opencv and facerecognation libraries in python library are relatively good libraries for face recognition introduction, but they are still not good for application up. When testing the program, I found that because I have to go through each frame of video for a lot of calculations. It caused the video to run very laggy. Very difficult to run properly. Next I planned to automatically save the video as a video and then make full use of the cpu for multi-processing, but the result was still not good. As a result, the project was not completed before the end of the internship. Also, there was no team and lack of communication. So it led to slow development of the project.

Face Recognition (V2).
Requirement.
Input: Input video with Face Recognation
Processing.
Process 1: Save the video
Process 2: Collect the saved video and then do the face recognition process
Save to database
Compare with data in database
Database :
Create database.
Table attributes (5): name (VARCHAR(50)), picture (BLOB), code (BLOB), face number (int PRIMARY KEY AUTO_INCREMENT), time (VARCHAR(50))

Collecting data.
Function 1 (parameters: picture, code) --> read in the unavailable face picture and code
main body
no return value
Function 2 (no arguments) --> call all faces
Main
return the list of encoding values

Function 3 (no arguments) --> call the whole corresponding face ID
Main
return the corresponding face ID
Function 4: (no parameters) Import the corresponding time (time).
main body
no return value

Function 5: (no parameter) clear time data
Main
No return value
*** Translated with www.DeepL.com/Translator (free version) ***









