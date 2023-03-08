def test():
  "--- test function ---" ;
  param = [
    ([[1, 9, 20, 22, 23, 33, 37, 40, 54, 63, 67, 68, 80, 81, 82, 84, 94], [11, 11, 14, 16, 28, 34, 40, 48, 49, 51, 60, 71, 81, 83, 93, 96, 98], [6, 14, 21, 22, 32, 40, 45, 47, 54, 76, 77, 80, 81, 85, 88, 90, 98], [6, 12, 20, 25, 29, 30, 36, 41, 44, 50, 76, 78, 80, 81, 90, 94, 99], [3, 5, 7, 10, 12, 14, 14, 19, 22, 28, 38, 40, 44, 46, 55, 77, 83], [1, 5, 21, 22, 27, 37, 44, 45, 48, 55, 56, 59, 64, 64, 73, 76, 83], [6, 26, 30, 31, 31, 37, 42, 57, 63, 68, 81, 85, 87, 96, 96, 97, 98], [3, 4, 22, 23, 36, 51, 54, 57, 57, 61, 70, 71, 74, 78, 79, 80, 93], [4, 4, 16, 18, 27, 52, 53, 54, 62, 64, 65, 78, 82, 83, 88, 89, 94], [2, 6, 8, 24, 34, 38, 40, 41, 43, 44, 46, 57, 59, 61, 63, 84, 93], [11, 11, 30, 45, 48, 52, 62, 64, 65, 66, 67, 75, 80, 87, 93, 96, 96], [16, 47, 56, 57, 67, 69, 77, 78, 79, 82, 83, 84, 88, 89, 91, 95, 97], [3, 9, 13, 24, 37, 48, 49, 52, 52, 68, 68, 72, 72, 78, 78, 94, 98], [3, 13, 18, 23, 23, 34, 35, 36, 36, 38, 41, 55, 57, 68, 75, 83, 87], [5, 23, 23, 31, 31, 33, 34, 45, 45, 48, 54, 60, 62, 71, 71, 73, 78], [3, 3, 4, 5, 8, 17, 19, 20, 29, 49, 61, 69, 71, 74, 86, 87, 88], [5, 12, 14, 19, 27, 28, 29, 30, 31, 33, 39, 40, 79, 80, 83, 83, 87]],10,13,),
    ([[94, 56, 74, -2, 26, -96, -62, 50, 58, -52, 4, 72, 98, -66, -80, -18, 12, -34, -36, 40, -48, 58, 2, -64, 14, -20, -94, 50, 58, 38, 12, 98, 18, 26, -64, 90, -48], [84, 70, 30, 22, -38, 98, 90, 42, -90, 54, 34, -44, -4, -88, 72, -70, 46, 56, 34, 96, 34, -92, 22, 94, 8, 16, 58, -36, 16, -34, 64, -20, 20, 50, 50, -30, 52], [-58, -46, 2, 58, -82, -8, 50, -82, 2, -28, -36, 12, -90, -88, -8, 86, -34, -24, 8, 4, 40, -56, 8, -12, 74, -96, 38, 50, -4, 6, -78, -36, 82, 14, 94, -74, 82], [-74, 40, -26, 24, 84, 98, -12, 98, 40, 14, -98, 44, -78, 98, 42, -34, -82, 68, 76, 40, 52, 46, -64, 26, 10, 64, -2, -84, -12, -40, -14, 82, 90, 46, -78, -4, 26], [82, -82, 32, -58, 86, 60, -4, -56, -86, -92, -58, 60, -94, -62, 44, 62, 58, 56, -16, -14, 8, -52, -26, 94, 70, -36, -16, -34, -42, 36, 94, -8, 62, -2, -30, -4, 28], [44, -90, -38, 34, -66, -90, 44, 30, 50, 14, -54, -88, -40, -22, -30, 42, -2, 70, -84, 60, -22, -4, 10, -92, 98, 90, 60, -10, 56, -16, -72, 34, 24, -2, -84, 76, -6], [76, -56, 10, 68, 2, -16, -24, 56, 80, -68, 96, 70, -42, 2, 44, -70, -24, 68, 36, -28, 84, -60, -96, 28, -64, 38, 62, 30, 86, -38, 94, 72, -22, 32, 14, -36, -54], [98, -46, -56, 48, 44, -90, 52, 14, -22, 72, 44, 80, 46, 34, -52, -64, -16, 64, -40, 18, 62, -62, 54, -2, 88, -2, -58, -86, 40, -2, 32, 90, -68, -76, 74, 48, 92], [0, -46, 38, 14, -26, 78, 16, 2, -90, -28, 92, -14, -36, -16, 32, 96, -30, 38, 32, -46, 88, 12, -6, -20, -8, 72, -50, -96, 20, -70, -50, -96, 38, -66, -36, -8, -76], [2, -98, -26, 48, 58, 58, -60, 22, -14, 30, -90, -12, 84, 28, 78, -32, 82, -12, -30, -88, -90, -32, -20, -46, -68, 16, -30, 52, 96, 84, -54, -50, -78, -44, 90, -58, -56], [78, -90, 2, 52, -8, 44, 14, -22, -12, 34, 30, -44, -66, 14, -72, -88, 38, -4, 88, 86, -52, -34, 28, 34, -46, -52, -30, -18, -94, 10, -60, 52, -34, -22, -64, 18, 22], [-54, 86, -62, -92, -58, -12, -42, -54, -42, -14, 34, -76, 50, -4, -64, 20, -88, -66, 42, -94, -54, -26, -92, -76, -6, -86, -92, 4, 82, -42, -66, -92, -74, 72, -22, -82, -98], [-80, -32, 62, -6, -48, -94, -8, 12, -98, -66, 50, -78, 42, 40, -70, -48, 86, 2, -60, 26, -24, 80, 18, -76, -20, 70, 72, -96, -56, -4, 94, -6, -2, -40, -54, -72, -22], [-76, 28, -48, -42, -50, -4, -38, -14, 26, 86, 48, -68, 90, 54, 92, -12, -60, 10, 80, 32, -80, -22, -72, 8, 24, 52, -62, -40, -20, -38, -16, -28, -70, 64, -34, -54, -20], [26, -46, 82, -76, -72, -18, 80, -96, 20, -80, 16, 12, 4, 32, -58, 94, 90, -58, 32, 38, -60, -68, 58, 58, -4, -14, 20, 22, -4, -6, 42, 18, -58, 62, 72, -86, 64], [-16, 98, 36, 58, 56, -40, -22, -60, 26, -64, 92, 96, -16, 32, 46, 32, -38, 92, -52, -78, -58, 4, -92, -68, -82, -96, -46, -52, -92, -10, 52, 90, -24, 50, -40, -4, -92], [64, 90, 14, -66, 30, -46, -74, -26, 10, -84, 84, -16, 30, 72, 40, -66, 4, 60, -52, 0, 94, -26, 68, -98, 28, 48, -50, 40, -30, 84, 58, -34, 68, 8, -58, -38, 80], [-6, 94, -38, 74, -22, 44, -8, -52, -38, 80, -30, 88, -2, 74, -64, -32, 44, 44, 92, -26, 38, 80, -10, 62, 40, -74, 50, 20, -50, 78, 30, 18, -80, 72, -80, 16, 74], [-26, -38, -90, -30, -18, 58, -76, 44, 26, -76, -50, 66, -94, 64, 42, -60, -16, -70, -28, -22, -62, 24, -60, 52, 22, 26, -94, -64, -12, 20, -16, -36, -28, 70, 52, 60, -66], [-94, -66, 82, -70, 36, 40, -54, -34, 88, -82, -18, 52, 36, 70, 40, -26, -22, 34, 84, 24, 52, -88, -74, -46, 30, 74, -58, -56, 54, 0, 48, -70, -10, -44, 70, -76, 38], [0, -24, 96, -96, 40, 24, -80, 44, -54, 36, -12, 74, -10, -60, -44, -46, -76, -14, 72, -22, -92, 50, 58, -16, -26, 68, -94, -84, -96, 84, 38, -12, -14, -48, 62, 94, 96], [-32, -96, 72, 4, 72, 46, 94, 74, 46, -52, 64, -82, -4, 6, -16, -58, -70, 26, 80, -70, 46, 48, 60, 54, -48, -28, 8, -12, 30, -34, -40, -40, 2, -80, 56, -96, -40], [-66, 64, 14, 96, -58, -42, 30, -20, 64, -96, 20, -54, -44, 42, 4, -30, -14, -8, -54, 62, -72, 34, 36, -18, -90, 36, 88, 58, -6, -96, -96, 74, -30, -44, 4, 32, 28], [-56, 14, -6, 48, 86, 2, 48, -40, 4, 20, -10, 2, 54, 8, -76, -64, -12, -54, -72, 14, -80, -64, 4, 0, -82, -76, -10, -68, -4, 4, 36, 32, -96, 28, 86, -34, 44], [40, 56, 0, -64, -82, 48, -68, 76, -28, 76, 90, 74, 68, 8, -4, -48, -62, 86, 6, 32, 54, -38, 48, -36, -50, -44, -14, 20, -50, -34, 52, 48, -82, 84, 84, -12, 14], [52, -6, -62, 90, -34, -64, -58, -76, 46, -30, -44, 4, -4, -48, -96, -52, 10, -16, -92, -58, 64, -26, -36, -2, -48, -4, -46, 40, -70, 84, 22, 84, -4, -58, 14, 44, 78], [38, 44, 36, -54, 80, -46, -52, 20, -34, 96, 18, -80, 20, 88, -2, 24, 54, 48, 86, 34, 84, -76, -58, 34, 22, -58, 54, -28, 98, 52, -42, 16, 28, 72, -60, -20, 54], [40, -80, 58, 60, 44, -66, -32, -90, -98, -8, 60, -50, 78, -70, 30, -60, 82, 34, 48, 6, -68, 6, -30, 58, -66, -20, -6, -48, -28, -8, -12, 52, -84, -22, 80, 54, -66], [16, 86, 6, 44, 36, 0, 92, 2, -92, 32, 80, 80, -88, -54, 26, -4, 50, -86, 58, -76, 44, 44, 88, -84, -22, -74, 68, 84, 44, 86, 12, -72, 56, -36, 36, 52, -38], [88, 48, 88, -78, 16, 78, 8, -60, -70, -74, -6, 96, -84, -42, 92, -26, 36, -28, -50, 96, -8, -70, 54, -60, -50, 60, 64, 22, -6, 32, -66, 22, -70, -40, 22, 92, 38], [-30, 98, -48, 58, -82, -54, 68, 88, -42, 16, -52, 42, -48, 0, 94, -92, 0, 66, -48, 66, -96, -6, -82, -98, 36, -90, 66, -68, -42, 32, 78, -8, -36, 52, 88, -46, 44], [-26, 28, 60, -74, -6, -38, -68, -14, 4, 20, 14, 84, -48, 24, -74, 4, 84, -28, -34, 2, 94, 2, 98, 44, -86, -14, 36, -94, -74, -60, 28, -98, -50, -30, 62, 38, 92], [44, -72, -38, 94, 38, -4, -58, -6, 36, 16, -74, 60, -84, -2, -58, 38, -30, 56, 18, 70, 34, 14, 70, -82, -78, -38, 50, -10, -16, -8, -98, 52, 46, 10, -80, -16, 94], [-94, -86, 86, 46, -64, -96, 60, 34, -18, 42, -52, 36, 76, 16, -48, 10, -96, -2, 52, 50, -16, 48, 0, -12, 64, -46, -32, -68, 58, 6, 50, -70, -82, 42, 0, -22, 26], [64, -8, -2, 54, 26, -62, 66, -10, 0, -20, 60, -98, -76, -72, 4, 88, 82, 82, 32, -88, -34, -16, -94, -92, -72, -72, 64, -54, -80, 52, 68, -36, -82, -20, 58, 38, 18], [-20, 26, 66, -4, -82, 56, 38, -32, -22, -50, 78, -74, 96, -44, 10, -6, -26, 44, -36, -8, 82, -86, -46, -24, -58, -50, -68, 10, 70, -68, 56, -38, -18, -14, 60, -28, 98], [98, -60, 44, -42, 78, 66, 38, -6, -78, 34, 26, 50, 26, 26, -60, -78, 86, 44, -86, 52, 56, 52, -46, 4, -24, -98, 92, -10, -80, -40, 86, 66, -66, -40, 84, -66, 16]],23,26,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],17,24,),
    ([[21, 51, 70, 93, 45, 29, 18, 47, 7, 9, 76], [23, 91, 12, 44, 91, 43, 81, 14, 49, 15, 85], [13, 4, 66, 25, 16, 75, 76, 95, 15, 78, 84], [56, 65, 67, 56, 49, 67, 52, 82, 15, 18, 89], [73, 95, 91, 73, 55, 27, 7, 43, 76, 43, 28], [80, 87, 66, 90, 96, 46, 98, 75, 70, 15, 3], [31, 46, 81, 10, 39, 57, 96, 69, 71, 64, 58], [77, 13, 14, 96, 97, 65, 21, 27, 42, 84, 99], [92, 16, 10, 81, 61, 7, 47, 86, 15, 20, 94], [9, 55, 54, 28, 7, 26, 73, 10, 63, 83, 76], [62, 59, 30, 61, 98, 3, 22, 26, 95, 47, 13]],7,9,),
    ([[-82, -80, -70, -56, -36, -24, -18, 12, 28, 38, 78], [-56, -34, -32, 30, 32, 40, 56, 66, 76, 86, 94], [-98, -90, -80, -64, -18, 6, 66, 66, 76, 84, 90], [-88, -74, -58, -16, -16, -8, 22, 34, 46, 68, 82], [-74, -58, -52, -46, -16, 30, 32, 40, 56, 80, 98], [-74, -70, -40, -26, -12, 6, 10, 50, 66, 74, 76], [-92, -86, -58, -30, 20, 22, 22, 24, 32, 38, 52], [-84, -64, -24, 26, 28, 38, 38, 48, 64, 82, 92], [-90, -50, -50, -42, -24, 32, 36, 60, 64, 78, 96], [-98, -76, -48, -40, -34, -6, 58, 58, 64, 70, 90], [-78, -72, -64, -34, -24, -12, -12, -2, 80, 82, 84]],6,8,),
    ([[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1]],23,19,),
    ([[13, 13, 18, 19, 22, 24, 25, 27, 28, 28, 29, 30, 44, 46, 52, 56, 60, 67, 75, 75, 83, 84, 87, 98], [5, 9, 11, 14, 14, 21, 21, 28, 40, 46, 55, 56, 57, 58, 58, 59, 67, 69, 75, 76, 78, 79, 87, 88], [1, 5, 6, 6, 8, 13, 20, 37, 44, 47, 54, 58, 67, 69, 73, 86, 89, 90, 91, 94, 96, 98, 99, 99], [1, 4, 12, 13, 21, 23, 26, 28, 32, 38, 43, 44, 51, 53, 55, 57, 58, 59, 60, 66, 70, 76, 82, 98], [3, 3, 4, 5, 5, 8, 11, 12, 12, 14, 16, 29, 29, 31, 41, 44, 53, 55, 61, 61, 67, 71, 84, 92], [2, 3, 4, 5, 7, 7, 11, 16, 19, 33, 36, 36, 38, 41, 48, 52, 53, 59, 65, 65, 70, 82, 82, 91], [10, 12, 13, 19, 20, 24, 25, 29, 30, 32, 34, 43, 55, 55, 56, 58, 68, 73, 73, 74, 75, 80, 87, 98], [4, 4, 7, 8, 9, 17, 20, 24, 27, 28, 32, 38, 52, 59, 65, 75, 78, 80, 81, 81, 83, 84, 85, 89], [4, 4, 5, 5, 8, 8, 11, 17, 18, 21, 35, 41, 51, 52, 56, 62, 63, 63, 63, 65, 77, 86, 90, 92], [3, 8, 10, 14, 22, 42, 46, 48, 49, 52, 55, 57, 61, 62, 64, 69, 70, 78, 80, 87, 88, 95, 96, 97], [2, 6, 6, 10, 10, 17, 19, 20, 22, 22, 24, 31, 40, 45, 47, 56, 56, 63, 79, 81, 81, 83, 84, 95], [8, 9, 11, 16, 17, 17, 21, 22, 26, 34, 35, 49, 50, 51, 56, 63, 64, 64, 70, 73, 73, 75, 78, 97], [1, 5, 5, 8, 13, 15, 18, 19, 20, 22, 27, 28, 32, 35, 38, 47, 50, 56, 72, 76, 77, 80, 96, 96], [8, 20, 31, 36, 37, 38, 39, 40, 43, 46, 46, 51, 57, 65, 69, 72, 76, 81, 83, 91, 93, 96, 97, 99], [1, 5, 5, 10, 13, 15, 18, 21, 29, 42, 43, 46, 50, 58, 62, 64, 67, 70, 74, 75, 76, 90, 91, 98], [3, 3, 7, 11, 12, 13, 24, 30, 35, 37, 37, 46, 48, 51, 58, 67, 67, 71, 72, 73, 80, 86, 86, 90], [8, 13, 15, 23, 31, 33, 36, 50, 53, 56, 64, 64, 64, 65, 76, 76, 79, 80, 82, 84, 86, 88, 90, 98], [2, 2, 4, 4, 6, 10, 11, 11, 12, 15, 17, 20, 26, 26, 27, 36, 45, 58, 60, 61, 66, 75, 90, 90], [3, 6, 15, 19, 26, 30, 32, 33, 33, 33, 35, 36, 43, 43, 45, 52, 55, 59, 78, 83, 86, 88, 89, 91], [15, 19, 23, 26, 34, 40, 49, 52, 56, 57, 61, 72, 72, 74, 76, 77, 78, 80, 80, 86, 89, 93, 99, 99], [12, 16, 21, 23, 24, 27, 32, 37, 40, 44, 47, 49, 49, 61, 64, 66, 67, 68, 71, 74, 86, 87, 93, 98], [1, 1, 2, 9, 21, 25, 26, 26, 28, 29, 30, 32, 34, 37, 47, 50, 51, 53, 58, 61, 65, 90, 94, 95], [3, 9, 10, 13, 14, 14, 18, 22, 23, 30, 30, 33, 40, 44, 45, 49, 50, 51, 58, 61, 66, 69, 71, 73], [7, 9, 11, 17, 22, 25, 31, 36, 39, 40, 54, 58, 59, 61, 64, 65, 71, 72, 73, 80, 88, 89, 96, 98]],22,13,),
    ([[38, -78, 50, 72, -54, 66, 16, -12, 14], [82, -86, -22, 76, -66, 84, -36, 92, -44], [92, 58, -44, 96, 14, 62, 52, -34, -32], [-72, 70, -22, 56, 86, -34, 36, 36, 36], [6, -56, 70, 42, -72, 32, 36, -12, 64], [-70, -20, -60, 74, -84, 98, 14, 22, -80], [62, -64, -64, -20, 12, -8, 32, 24, 50], [-60, -84, -6, 18, -66, -58, -62, -82, 34], [-50, 98, 58, -80, 12, 58, -88, 72, 58]],4,4,),
    ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],31,19,),
    ([[84, 10, 44, 41, 67, 79, 29, 22, 76, 13, 25, 78, 49, 38, 41, 33, 67, 43, 72, 34, 37, 35, 1, 88, 97, 70, 29, 84, 90, 6, 26, 39, 69, 80, 82, 55, 23, 11, 56, 41, 24, 23, 44, 42, 80, 50, 66], [41, 63, 60, 11, 13, 95, 35, 38, 99, 34, 27, 51, 27, 8, 6, 65, 20, 87, 82, 6, 64, 87, 55, 43, 90, 36, 99, 91, 79, 82, 5, 91, 94, 45, 58, 80, 25, 82, 96, 50, 1, 47, 29, 45, 3, 13, 11], [67, 35, 69, 76, 5, 61, 46, 71, 66, 22, 43, 49, 82, 13, 78, 92, 46, 99, 88, 4, 12, 54, 29, 6, 92, 88, 38, 39, 10, 32, 4, 52, 50, 60, 46, 96, 80, 84, 24, 54, 6, 99, 82, 3, 90, 15, 48], [4, 14, 43, 59, 97, 81, 40, 63, 85, 87, 60, 11, 10, 73, 74, 88, 73, 5, 51, 17, 3, 89, 55, 19, 62, 54, 43, 81, 76, 31, 67, 68, 72, 22, 33, 94, 10, 7, 36, 49, 20, 67, 4, 62, 29, 97, 55], [54, 96, 20, 42, 73, 11, 59, 50, 29, 45, 10, 53, 88, 50, 27, 48, 17, 51, 58, 53, 12, 9, 4, 74, 31, 80, 98, 80, 46, 24, 52, 41, 5, 49, 54, 4, 32, 71, 78, 19, 52, 34, 18, 85, 89, 45, 88], [88, 75, 46, 96, 4, 73, 32, 55, 93, 84, 88, 61, 91, 39, 98, 2, 71, 20, 50, 22, 71, 66, 68, 19, 93, 20, 99, 89, 50, 77, 42, 5, 87, 90, 88, 94, 50, 90, 94, 17, 37, 81, 31, 78, 44, 17, 95], [60, 72, 44, 69, 75, 95, 41, 2, 54, 99, 40, 21, 4, 55, 29, 62, 13, 89, 30, 80, 27, 81, 59, 46, 35, 73, 54, 22, 16, 39, 74, 9, 60, 87, 82, 44, 99, 11, 88, 56, 57, 56, 95, 93, 25, 74, 57], [96, 48, 66, 6, 82, 66, 21, 3, 75, 51, 26, 58, 38, 54, 6, 81, 86, 50, 27, 4, 31, 65, 21, 39, 10, 38, 22, 34, 91, 94, 85, 63, 95, 24, 96, 14, 78, 36, 75, 20, 70, 53, 53, 88, 77, 44, 15], [81, 60, 57, 34, 69, 95, 47, 13, 79, 77, 39, 2, 61, 41, 88, 81, 38, 80, 62, 24, 81, 80, 53, 96, 96, 10, 55, 27, 10, 32, 38, 88, 66, 17, 84, 4, 58, 48, 94, 47, 4, 91, 78, 85, 84, 17, 53], [75, 85, 85, 64, 87, 39, 23, 36, 94, 10, 99, 38, 55, 50, 83, 78, 47, 98, 20, 24, 6, 18, 2, 26, 28, 42, 40, 88, 32, 31, 33, 58, 81, 34, 53, 43, 60, 1, 44, 55, 85, 21, 96, 33, 77, 85, 8], [10, 34, 81, 70, 60, 50, 54, 82, 53, 30, 84, 60, 92, 81, 90, 62, 46, 16, 75, 33, 53, 21, 96, 87, 79, 48, 57, 54, 59, 71, 78, 90, 28, 75, 11, 98, 76, 54, 75, 73, 98, 84, 25, 63, 51, 51, 42], [1, 64, 2, 2, 58, 39, 10, 29, 38, 95, 52, 68, 13, 82, 26, 1, 9, 93, 66, 42, 46, 54, 46, 58, 38, 68, 4, 92, 63, 17, 50, 21, 28, 74, 10, 95, 21, 50, 66, 58, 23, 51, 80, 67, 96, 7, 60], [84, 17, 10, 64, 11, 72, 15, 93, 32, 51, 15, 8, 13, 76, 58, 52, 48, 70, 30, 91, 58, 56, 73, 36, 75, 47, 90, 80, 6, 71, 24, 42, 59, 77, 56, 80, 37, 20, 82, 2, 6, 40, 56, 12, 70, 26, 25], [44, 16, 42, 51, 83, 3, 71, 30, 78, 53, 89, 99, 30, 51, 38, 76, 78, 81, 48, 73, 24, 11, 68, 68, 65, 2, 21, 92, 42, 45, 68, 95, 12, 68, 75, 45, 70, 92, 88, 16, 37, 25, 53, 56, 89, 87, 27], [82, 34, 78, 97, 29, 4, 25, 82, 78, 90, 41, 23, 29, 84, 52, 6, 46, 12, 32, 97, 30, 36, 68, 86, 25, 76, 48, 4, 39, 36, 44, 46, 3, 3, 55, 4, 64, 50, 54, 39, 82, 79, 18, 84, 39, 89, 5], [71, 39, 31, 9, 36, 51, 56, 34, 72, 65, 50, 29, 62, 26, 72, 43, 99, 85, 43, 3, 33, 88, 61, 58, 10, 38, 22, 62, 74, 2, 53, 50, 27, 65, 45, 41, 65, 2, 32, 62, 36, 89, 45, 59, 95, 4, 36], [86, 32, 63, 7, 72, 52, 79, 87, 80, 48, 12, 54, 58, 42, 61, 70, 10, 41, 81, 92, 41, 48, 41, 12, 84, 18, 57, 74, 80, 25, 88, 57, 98, 59, 99, 4, 13, 44, 45, 77, 52, 9, 6, 41, 95, 81, 1], [74, 35, 5, 73, 39, 71, 12, 65, 71, 42, 46, 93, 56, 72, 22, 14, 69, 11, 68, 31, 86, 62, 83, 69, 75, 31, 18, 37, 97, 84, 67, 5, 36, 75, 4, 26, 43, 41, 27, 2, 29, 4, 88, 23, 29, 5, 23], [35, 65, 33, 90, 99, 89, 26, 89, 61, 99, 17, 68, 1, 70, 99, 24, 11, 49, 97, 26, 72, 49, 5, 21, 3, 85, 48, 14, 7, 78, 76, 70, 56, 58, 61, 61, 71, 65, 92, 17, 39, 37, 24, 16, 32, 50, 21], [53, 52, 57, 38, 72, 57, 23, 88, 57, 43, 7, 15, 41, 33, 28, 62, 90, 50, 59, 43, 54, 92, 30, 15, 28, 50, 66, 5, 83, 5, 98, 33, 57, 37, 40, 20, 50, 70, 62, 7, 8, 91, 75, 65, 27, 68, 37], [4, 31, 38, 23, 45, 69, 99, 5, 26, 38, 11, 41, 47, 77, 28, 36, 50, 63, 32, 33, 72, 94, 76, 36, 55, 72, 73, 33, 62, 46, 60, 22, 40, 73, 56, 22, 5, 99, 85, 51, 15, 62, 24, 2, 80, 71, 82], [96, 50, 12, 21, 14, 72, 43, 56, 47, 57, 80, 17, 70, 80, 20, 40, 50, 80, 27, 45, 59, 18, 64, 79, 19, 70, 79, 38, 35, 77, 56, 35, 83, 6, 62, 32, 54, 83, 97, 3, 22, 53, 95, 39, 65, 30, 77], [84, 95, 21, 24, 16, 74, 75, 2, 87, 59, 32, 37, 39, 73, 27, 37, 79, 59, 68, 49, 28, 20, 21, 61, 74, 44, 25, 72, 32, 77, 18, 57, 32, 48, 75, 29, 35, 75, 30, 63, 88, 51, 3, 64, 90, 30, 34], [3, 68, 51, 85, 86, 63, 14, 75, 18, 2, 3, 77, 89, 51, 38, 29, 66, 51, 54, 42, 34, 11, 19, 27, 73, 57, 92, 45, 25, 47, 41, 83, 38, 33, 60, 65, 57, 54, 53, 84, 47, 25, 58, 51, 74, 28, 92], [32, 56, 38, 3, 51, 13, 26, 84, 98, 85, 45, 76, 20, 17, 38, 11, 31, 25, 22, 48, 23, 76, 70, 9, 54, 62, 49, 11, 66, 30, 64, 25, 5, 48, 82, 86, 58, 21, 89, 22, 28, 70, 55, 93, 3, 22, 27], [98, 13, 15, 32, 61, 94, 72, 63, 84, 74, 78, 31, 88, 61, 19, 84, 89, 69, 93, 89, 11, 85, 45, 38, 2, 26, 89, 27, 39, 10, 1, 90, 8, 24, 47, 75, 58, 65, 58, 98, 8, 25, 6, 72, 23, 67, 15], [32, 48, 68, 80, 20, 97, 45, 58, 75, 99, 27, 28, 85, 62, 72, 89, 75, 20, 25, 29, 48, 94, 69, 79, 40, 44, 14, 95, 45, 43, 41, 59, 74, 86, 60, 25, 67, 52, 28, 48, 6, 61, 15, 6, 53, 48, 41], [68, 83, 68, 45, 1, 20, 81, 38, 69, 15, 98, 57, 90, 59, 15, 41, 71, 93, 44, 59, 28, 35, 96, 56, 73, 31, 88, 32, 12, 76, 18, 65, 85, 7, 30, 32, 88, 10, 41, 38, 81, 2, 12, 62, 24, 97, 67], [63, 22, 74, 40, 8, 90, 97, 50, 54, 82, 91, 23, 93, 34, 2, 34, 89, 11, 30, 34, 76, 47, 58, 7, 56, 85, 61, 54, 73, 61, 50, 15, 99, 94, 66, 53, 86, 44, 5, 77, 11, 69, 83, 18, 50, 44, 60], [71, 53, 43, 3, 33, 22, 41, 93, 13, 83, 59, 80, 53, 70, 55, 59, 87, 28, 95, 33, 63, 6, 78, 91, 85, 84, 10, 43, 35, 26, 46, 90, 17, 91, 43, 55, 22, 63, 19, 56, 58, 78, 18, 15, 12, 16, 10], [22, 77, 48, 54, 93, 66, 3, 92, 1, 60, 45, 16, 96, 84, 53, 99, 57, 79, 18, 77, 87, 47, 20, 86, 80, 97, 54, 54, 13, 16, 34, 67, 61, 20, 40, 96, 92, 13, 45, 63, 45, 28, 85, 47, 17, 78, 26], [38, 88, 52, 35, 4, 85, 85, 27, 66, 45, 39, 59, 50, 38, 41, 64, 72, 2, 63, 43, 74, 55, 21, 91, 62, 98, 78, 53, 38, 79, 17, 12, 12, 66, 56, 7, 16, 24, 58, 95, 30, 37, 50, 54, 27, 90, 99], [29, 32, 35, 3, 44, 64, 80, 34, 10, 94, 70, 3, 73, 2, 48, 94, 87, 9, 32, 41, 32, 13, 68, 22, 93, 74, 43, 29, 61, 1, 20, 94, 53, 2, 50, 77, 42, 6, 90, 82, 23, 75, 67, 77, 71, 50, 53], [75, 62, 43, 96, 10, 99, 28, 61, 91, 85, 81, 13, 87, 25, 89, 47, 72, 68, 34, 82, 77, 91, 43, 84, 28, 63, 19, 13, 72, 34, 72, 9, 49, 53, 86, 16, 55, 91, 36, 44, 35, 81, 44, 40, 80, 87, 62], [62, 74, 89, 35, 2, 44, 8, 7, 41, 80, 55, 16, 55, 63, 4, 57, 43, 5, 80, 92, 64, 16, 4, 42, 36, 83, 38, 78, 81, 19, 17, 4, 42, 97, 86, 74, 29, 11, 71, 94, 61, 88, 75, 46, 35, 95, 80], [47, 23, 32, 47, 25, 17, 20, 62, 5, 96, 40, 29, 37, 47, 98, 30, 38, 60, 49, 38, 12, 99, 33, 85, 63, 6, 65, 51, 77, 48, 13, 34, 74, 35, 86, 22, 56, 13, 36, 5, 60, 30, 1, 57, 95, 31, 43], [95, 96, 48, 82, 10, 53, 29, 64, 84, 45, 16, 44, 52, 69, 73, 63, 3, 23, 84, 89, 50, 85, 2, 1, 43, 60, 45, 33, 32, 12, 8, 89, 80, 81, 46, 55, 51, 66, 8, 24, 69, 84, 74, 92, 31, 27, 56], [98, 48, 25, 59, 80, 63, 46, 61, 26, 66, 96, 56, 29, 5, 41, 63, 54, 75, 96, 50, 15, 48, 20, 51, 91, 37, 43, 31, 70, 29, 44, 36, 60, 8, 31, 37, 3, 72, 40, 99, 43, 6, 62, 91, 4, 92, 48], [76, 56, 21, 97, 47, 59, 28, 97, 5, 94, 98, 45, 69, 9, 67, 3, 62, 28, 4, 41, 68, 48, 53, 41, 18, 46, 64, 62, 49, 72, 6, 53, 17, 40, 81, 26, 14, 67, 88, 84, 61, 16, 10, 29, 72, 14, 31], [28, 54, 78, 42, 85, 78, 69, 26, 92, 67, 17, 39, 74, 5, 7, 57, 82, 48, 82, 62, 86, 4, 3, 13, 29, 93, 45, 83, 3, 58, 92, 68, 6, 30, 22, 80, 16, 17, 56, 45, 16, 1, 34, 92, 38, 35, 12], [13, 68, 72, 1, 28, 7, 74, 89, 41, 19, 5, 30, 70, 94, 74, 9, 96, 57, 25, 11, 68, 37, 90, 46, 79, 20, 5, 69, 31, 95, 83, 39, 20, 13, 69, 57, 13, 11, 35, 5, 33, 23, 85, 4, 55, 44, 13], [26, 30, 70, 63, 1, 16, 36, 98, 48, 11, 15, 97, 86, 19, 37, 78, 14, 33, 72, 22, 60, 43, 32, 69, 23, 54, 11, 52, 82, 80, 46, 34, 63, 82, 18, 93, 44, 80, 72, 97, 44, 22, 14, 91, 46, 12, 84], [34, 11, 15, 1, 99, 90, 69, 71, 4, 69, 18, 45, 62, 2, 67, 35, 33, 49, 37, 42, 80, 39, 59, 22, 87, 68, 87, 25, 20, 62, 93, 72, 59, 76, 5, 19, 42, 74, 21, 60, 33, 11, 68, 1, 1, 40, 15], [75, 49, 19, 39, 48, 35, 59, 8, 23, 61, 70, 63, 89, 32, 61, 42, 83, 44, 63, 94, 24, 26, 74, 71, 99, 58, 57, 21, 54, 40, 99, 73, 34, 14, 41, 68, 51, 6, 11, 30, 28, 72, 80, 22, 16, 21, 24], [51, 47, 70, 30, 18, 56, 48, 68, 97, 68, 75, 67, 51, 25, 97, 45, 37, 9, 75, 40, 96, 78, 7, 9, 23, 54, 29, 78, 37, 16, 99, 63, 77, 46, 75, 94, 26, 78, 3, 98, 23, 4, 36, 41, 15, 38, 70], [76, 50, 47, 76, 53, 43, 14, 38, 29, 5, 39, 85, 21, 4, 32, 19, 40, 47, 38, 82, 67, 96, 51, 14, 32, 47, 74, 81, 62, 73, 81, 42, 67, 12, 35, 33, 76, 51, 13, 17, 1, 59, 32, 98, 43, 37, 6], [92, 99, 52, 85, 57, 24, 71, 71, 63, 59, 85, 11, 15, 57, 24, 55, 34, 57, 92, 81, 60, 4, 53, 12, 12, 93, 99, 12, 94, 76, 51, 56, 71, 11, 16, 91, 91, 72, 51, 1, 37, 56, 2, 71, 53, 1, 98]],37,43,)
        ]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(mat, n, x):
  i = 0
  j = n - 1
  while(i < n and j >= 0):
    if(mat[i][j] == x):
      print("n Found at ", i, ", ", j)
      return 1
    if(mat[i][j] > x): j -= 1
    else: i += 1
  print("Element not found")
  return 0
"-----------------"
test()
