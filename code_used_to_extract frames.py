import cv2
video = cv2.VideoCapture('Sample.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
tim = 18

for i in range(1,61):

    frame_id = int(fps*(tim))
    tim = tim + 0.25
    video.set(cv2.CAP_PROP_POS_FRAMES,frame_id)
    ret, frame = video.read()
    fvar = 'frame_without_plane_' + str(i)+'.png'
    cv2.imwrite(fvar,frame)


