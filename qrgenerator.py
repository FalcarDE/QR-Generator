import qrcode
class qrgenerator:
    def Input_Filename(self):
        Raw_Filname = input("Please insert the Name of your file: ")
        Manipulate_Filname = Raw_Filname + ".png"
        return Manipulate_Filname

    def Input_Info(self):
        Raw_InputInfo = input("Please insert you Data or weblink: ")
        Manipulate_Info = Raw_InputInfo
        return Manipulate_Info

    def qr_generator(self,_filename,_ManipulationInfo):
        qr_image = qrcode.make(_ManipulationInfo)
        qr_image.save(_filename)

Qr_Object = qrgenerator()
filename = Qr_Object.Input_Filename()
Information = Qr_Object.Input_Info()
Qr_Object.qr_generator(filename, Information)