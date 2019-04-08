import wx
class ConfigurationFrame(wx.Frame):
	

	def __init__(self, parent):
		#CLASS VARIABLES
		self.PIDS = []
		self.PNAMES = []
		self.DB_USER =""
		self.DB_PW =""
		self.DB_HOST=""
		self.BROKER_IP=""
		self.STORAGE_MODE=""
		self.WINDOW_SIZE=3
		self.LOGGING_LEVEL =""
		#PARENT FRAME AND PANEL
		wx.Frame.__init__(self, parent,title="MQTT-IDS : Configure",size=(370,320))
		panel = wx.Panel(self)

		#CONTENT
		self.disclaimer = wx.StaticText(panel, label="This tool is meant for evaluation and testing purposes only.", pos=(5, 5))

		
		wx.StaticLine(panel,pos=(5,25),size=(340,2),style=wx.LI_HORIZONTAL)
		wx.StaticText(panel, pos=(5,35) ,label="PIDS, comma separated:")
		self.PIDS_TXTBOX = wx.TextCtrl(panel, pos=(5,55),size=(150,20),style = wx.TE_PROCESS_ENTER,name="PIDS")
		self.PIDS_TXTBOX.Bind(wx.EVT_TEXT_ENTER,self.value_entered)

		wx.StaticText(panel, pos=(5,75) ,label="PNames, comma separated:")
		self.PNAMES_TXTBOX = wx.TextCtrl(panel,pos=(5,95),size=(150,20),style = wx.TE_PROCESS_ENTER,name="PNAMES")
		self.PNAMES_TXTBOX.Bind(wx.EVT_TEXT_ENTER,self.value_entered)

		wx.StaticText(panel, pos=(5,115) ,label="Database username")
		self.DB_USER_TXTBOX = wx.TextCtrl(panel,pos=(5,135),size=(150,20),style = wx.TE_PROCESS_ENTER,name="DB_USER")
		self.DB_USER_TXTBOX.Bind(wx.EVT_TEXT_ENTER,self.value_entered)

		wx.StaticText(panel, pos=(5,155) ,label="Database password")
		self.DB_PW_TXTBOX = wx.TextCtrl(panel,pos=(5,175),size=(150,20),style = wx.TE_PROCESS_ENTER|wx.TE_PASSWORD,name="DB_PW")
		self.DB_PW_TXTBOX.Bind(wx.EVT_TEXT_ENTER,self.value_entered)

		wx.StaticText(panel, pos=(5,195), label ="Logging Level")
		self.LOGGING_LEVEL_COMBOBOX = wx.ComboBox(panel,pos=(5,215),size=(150,20),style=wx.CB_READONLY|wx.CB_DROPDOWN,choices = ('INFO','DEBUG','WARNING','CRITICAL'))
		self.LOGGING_LEVEL_COMBOBOX.Bind(wx.EVT_COMBOBOX,self.pick_combobox)

		wx.StaticText(panel, pos=(195,35) ,label="Database host")
		self.DB_HOST_TXTBOX = wx.TextCtrl(panel, pos=(195,55),size=(150,20),style = wx.TE_PROCESS_ENTER,name="DB_HOST")
		self.DB_HOST_TXTBOX.Bind(wx.EVT_TEXT_ENTER,self.value_entered)
		
		wx.StaticText(panel, pos=(195,75) ,label="Broker IP")
		self.BROKER_IP_TXTBOX = wx.TextCtrl(panel, pos=(195,95),size=(150,20),style = wx.TE_PROCESS_ENTER,name="BROKER_IP")
		self.BROKER_IP_TXTBOX.Bind(wx.EVT_TEXT_ENTER,self.value_entered)

		wx.StaticText(panel,pos=(195,115),label="Pick Storage Mode:")
		self.STORAGE_MODE_COMBOBOX = wx.ComboBox(panel,pos=(195,135),size=(150,20),style=wx.CB_READONLY|wx.CB_DROPDOWN,choices=('Enabled','Disabled'))
		self.STORAGE_MODE_COMBOBOX.Bind(wx.EVT_COMBOBOX,self.pick_combobox)

		wx.StaticText(panel,pos=(195,155),label="Pick Window Size:")
		self.WINDOW_SIZE_COMBOBOX = wx.ComboBox(panel,pos=(195,175),size=(150,20),style=wx.CB_READONLY|wx.CB_DROPDOWN,choices=["3","4","5","6","7","8","9"])
		self.WINDOW_SIZE_COMBOBOX.Bind(wx.EVT_COMBOBOX,self.pick_windowsize)




		self.EXPORT_BUTTON = wx.Button(panel,pos=(5,250), size=(340,20),label="Export config!")
		self.EXPORT_BUTTON.Bind(wx.EVT_BUTTON,self.export)




		#SHOW CONTENT
		self.Show()
	#HELPER AND CALLBACK FUNCTIONS
	def value_entered(self,event):
		if(event.GetEventObject().GetName()=="PIDS"):
			self.PIDS = self.PIDS_TXTBOX.GetValue().split(",")
			print(type(self.PIDS))
			print(self.PIDS)
		elif(event.GetEventObject().GetName()=="PNAMES"):
			self.PNAMES = self.PNAMES_TXTBOX.GetValue().split(",")
			print(type(self.PNAMES))
			print(self.PNAMES)
		elif(event.GetEventObject().GetName()=="DB_USER"):
			self.DB_USER = self.DB_USER_TXTBOX.GetValue()
			print(type(self.DB_USER))
			print(self.DB_USER)
		elif(event.GetEventObject().GetName()=="DB_PW"):
			self.DB_PW = self.DB_PW_TXTBOX.GetValue()
			self.DB_PW_TXTBOX.Clear()
		elif(event.GetEventObject().GetName()=="DB_HOST"):
			self.DB_HOST = self.DB_HOST_TXTBOX.GetValue()
		elif(event.GetEventObject().GetName()=="BROKER_IP"):
			self.BROKER_IP = self.BROKER_IP_TXTBOX.GetValue()

	def pick_combobox(self,event):
		if self.STORAGE_MODE_COMBOBOX.GetValue()=='Enabled':
			self.STORAGE_MODE=True
			print(type(event))
			print("True")
		elif self.STORAGE_MODE_COMBOBOX.GetValue()=='Disabled':
			self.STORAGE_MODE=False
			print("False")
		elif self.LOGGING_LEVEL_COMBOBOX.GetValue()=='INFO':
			self.LOGGING_LEVEL='INFO'
		elif self.LOGGING_LEVEL_COMBOBOX.GetValue()=='DEBUG':
			self.LOGGING_LEVEL='DEBUG'
		elif self.LOGGING_LEVEL_COMBOBOX.GetValue()=='WARNING':
			self.LOGGING_LEVEL='WARNING'
		elif self.LOGGING_LEVEL_COMBOBOX.GetValue()=='CRITICAL':
			self.LOGGING_LEVEL='CRITICAL'

	def pick_windowsize(self,event):
		self.WINDOW_SIZE = self.WINDOW_SIZE_COMBOBOX.GetValue()

	def export(self,event):
		import lxml
		from lxml import etree
		et = etree.Element("CONFIG")

		PIDS_XML = etree.SubElement(et,"PIDS")
		for PID in self.PIDS:
			ProcessID = etree.SubElement(PIDS_XML,"PID")
			ProcessID.text = str(PID)
		PNAMES_XML = etree.SubElement(et,"PNAMES")
		for PNAME in self.PNAMES:
			ProcessName = etree.SubElement(PNAMES_XML,"PNAME")
			ProcessName.text = PNAME

		WINDOW_SIZE_XML = etree.SubElement(et,"WINDOW_SIZE")
		WINDOW_SIZE_XML.text = str(self.WINDOW_SIZE)

		DB_USER_XML       = etree.SubElement(et,"DB_USER")
		DB_USER_XML.text  = self.DB_USER
		DB_PW_XML         = etree.SubElement(et,"DB_PW")
		DB_PW_XML.text    = self.DB_PW
		DB_HOST_XML	  = etree.SubElement(et,"DB_HOST")
		DB_HOST_XML.text  = self.DB_HOST
		BROKER_IP_XML     = etree.SubElement(et,"BROKER_IP")
		BROKER_IP_XML.text= self.BROKER_IP
		STORAGE_MODE_XML  = etree.SubElement(et,"STORAGE_MODE")
		STORAGE_MODE_XML.text = str(self.STORAGE_MODE)
		LOGGING_LEVEL_XML = etree.SubElement(et,"LOGGINGLEVEL")
		LOGGING_LEVEL_XML.text = str(self.LOGGING_LEVEL)


		with open('./configuration.xml', 'wb') as f:
			f.write(etree.tostring(et,pretty_print=True,xml_declaration=True,encoding="utf-8"))
			
		

app = wx.App(False)
ConfigurationFrame(None)
app.MainLoop()