import wx  # 导入wx模块


class ButtonFrame(wx.Frame):
    ClickNum = 0  # 定义变量

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Button Demo',
                          size=(300, 200))  # 初始化窗口信息

        panel = wx.Panel(self, -1)  # 创建面板
        self.button = wx.Button(
            panel, -1, "OFF", pos=(50, 50), size=(50, 30))  # 在面板上添加控件
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)  # 将回调函数与按键事件绑定

        self.box = wx.CheckBox(panel, -1, "Checkbox",
                               pos=(150, 50), size=(80, 20))  # 创建控件复选框
        self.Bind(wx.EVT_CHECKBOX, self.ChoseBox_Event, self.box)  # 绑定事件
        self.box.SetValue(False)  # 设置当前是否被选中

        sampleList = ['COM1', 'COM2', 'COM3', 'COM4',
                      'COM5', 'COM6', 'COM7', 'COM8', 'COM9']

        self.Info_txt = wx.StaticText(panel, -1, "串口号", (15, 20))
        self.ChoiceOption = wx.Choice(panel, -1, (80, 18), choices=sampleList)
        self.Bind(wx.EVT_CHOICE, self.ChoseBox1, self.ChoiceOption)  # 绑定事件

        # 系统事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, evt):
        '''关闭窗口事件函数'''
        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示',
                               wx.YES_NO | wx.ICON_QUESTION)
        if(dlg.ShowModal() == wx.ID_YES):
            self.Destroy()

    def ChoseBox1(self, event):
        ''' 下拉列表回调函数回调函数'''
        print(event.GetString()+"被选中")

    def ChoseBox_Event(self, event):  # 事件回调函数
        print(self.box.GetValue())  # 打印True 证明复选框已经被选中 False 则反之

    def OnClick(self, event):  # 回调函数事件
        self.button.SetLabel("ON")  # 设置
        self.ClickNum += 1
        if self.ClickNum % 2 == 1:  # 根据按下次数判断
            self.button.SetLabel("ON")  # 修改按键的标签
            print(self.button.GetLabel())  # 打印信息（返回按键的标签信息）
        else:
            self.button.SetLabel("OFF")
            self.ClickNum = 0
            print(self.button.GetLabel())

 # 主函数入口


if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.PySimpleApp()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()
