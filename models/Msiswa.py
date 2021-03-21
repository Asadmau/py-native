class Msiswa(object):
    mahasiswa = [{
        'nim': '123',
        'nama': 'asad',
        'email': 'asad@gmail.com'
    }]

    def getAll(self):
        return  self.mahasiswa
    def setAll(self, new_mahasiswa):
        self.mahasiswa = new_mahasiswa
