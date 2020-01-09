import plistlib
fileName = 'pl1.xml'
plist = plistlib.readPlist(fileName)
tracks = plist['Tracks']
trackNames = {}
for trackID, track in tracks.items():
    try:
        name = track['Name']
        duration = track['Total Time']
        if name in trackNames:
            if duration // 1000 == trackNames[name][0] // 1000:
                count = trackNames[name][1]
                trackNames[name] = (duration, count + 1)
            else:
                trackNames[name] = (duration, 1)
                print(type(trackName))
    except:
        pass

dups = []
