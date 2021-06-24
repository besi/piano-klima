import machine, uos

sd = machine.SDCard(slot=2)
uos.mount(sd, "/sd")  # mount
uos.listdir('/sd')    # list directory contents
path = '/sd/test.csv'

# Create the file
open(path, 'a').close()

f = open(path, 'a')
t = time.time()
f.write('{} {} {} {}\n'.format(t, 1, 2, 3))
f.close()

uos.umount('/sd')
