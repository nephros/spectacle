#!/usr/bin/python

import yaml,  sys
import re
import os
from spec import spec
from dsc import dsc


class RPMWriter():
    def __init__(self,  filename):
        self.filename = filename
        self.stream = file(filename, 'r')
        self.metadata = None
        self.extra = {}
        pass
    def dump(self):
        print yaml.dump(yaml.load(self.stream))
    def parse(self):
        self.metadata = yaml.load(self.stream)
    def parse_files(self, files):
        self.extra = {
                'PreUn': [],
                'Desktop': False,
                'Static': False,
                'Schema': False,
                'Schemas': [],
                'Lib': False,
                'Icon': False,
                'Service': False,
                'Info': False,
                'Infos': [],
                }
        for k,v in files.iteritems():
            for l in v:
                if re.match('.*\.info.*', l) and re.match('.*usr/share/info.*', l):
                    self.extra['PreUn'].append("/sbin/install-info")
                    self.extra['Infos'].append(l)
                    self.extra['Info'] = True
                if re.match('.*\.desktop$', l):
                    self.extra['Desktop'] = True
                if re.match('.*\.a$', l):
                    self.extra['Static'] = True
                if re.match('.*etc/rc.d/init.d.*', l) or re.match('.*etc/init.d.*', l):
                    self.extra['Service'] = True
                    self.extra['PreUn'].append("/sbin/chkconfig")
                    self.extra['PreUn'].append("/sbin/service")
                if re.match('.*\.so\..*', l):
                    self.extra['Lib'] = True
                if re.match('.*\.schema.*', l):
                    self.extra['Schema'] = True
                    self.extra['Schemas'].append(l)


    def parse_existing(selfs, file):
        sin = re.compile("^# >> ([^\s]+) (.*)")
        sout = re.compile("^# << ([^\s]+) (.*)")
        recording = []
        record = False
        files = {}
        install = {}
        build = {}
        for i in file.read().split("\n"):  
            matchin = sin.match(i)
            matchout = sout.match(i)
            if matchin:
                record = True
                recording = []
                continue
            if matchout:
                record = False
                if matchout.group(1) == "files" and not matchout.group(2):
                    files['main'] = recording
                elif matchout.group(1) == "files" and matchout.group(2):
                    files[matchout.group(2)] = recording
                elif matchout.group(1) == "install":
                    install[matchout.group(2)] = recording
                elif matchout.group(1) == "build":
                    build[matchout.group(2)] = recording
        
            if record:
                recording.append(i)
        usercontent = {"files" : files, "install": install, "build" : build}
        return usercontent

    def process(self):
        specfile = "%s.spec" %self.metadata['Name']
        if os.path.exists(specfile):
            print "file exists, patching..."
            file = open(specfile, "r")
            usercontent = self.parse_existing(file)
            file.close()
            self.parse_files(usercontent['files'])
            self.extra['content'] = usercontent
            nameSpace = {'metadata': self.metadata, 'extra': self.extra }
            t = spec(searchList=[nameSpace])
            a = str(t)
            file = open(specfile, "w")
            file.write(a)
            file.close()           
        else:
            print "Creating new spec file: %s" %specfile
            nameSpace = {'metadata': self.metadata, 'extra': self.extra }
            t = spec(searchList=[nameSpace])
            a = str(t)
            file = open(specfile, "w")
            file.write(a)
            file.close()

        #t = dsc(searchList=[nameSpace])
        #a = str(t)
        #print a


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        rpm = RPMWriter(filename)
        rpm.parse()
        rpm.process()
        print rpm.extra
