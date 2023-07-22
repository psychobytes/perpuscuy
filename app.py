#import module
from flask import Flask, url_for, redirect, request, render_template, session
from mysql import connector

#menghubungkan ke database
db = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'db_pbdperpus'
)
if db.is_connected():
    print("[!] Database Terhubung [!]")

app = Flask(__name__)
app.secret_key = 'inikeycuy'


@app.route('/login')
def login():
    return render_template ('login.html')

# ================================================belum jadi==================================
@app.route('/login-proses', methods=['POST', 'GET'])
def login_proses():
    # Output a message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cur = db.cursor()
        cur.execute('SELECT * FROM admin WHERE nama = %s AND nik = %s', (username, password,))
        # Fetch one record and return result
        account = cur.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = account[0]
            session['password'] = account[1]
            # Redirect to home page
            return redirect(url_for('admin'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('username', None)
   session.pop('password', None)
   # Redirect to login page
   return redirect(url_for('login'))

# =========================================index=====================================
@app.route('/', methods=['POST', 'GET'])
# function untuk menampilkan halaman index(check in)
def index():
    # ambil seluruh data dari tabel pengunjung
    cur = db.cursor()
    cur.execute("SELECT id_pengunjung, nama, alamat, tanggal, status FROM pengunjung ORDER BY id_pengunjung DESC")
    # global pengunjung
    pengunjung = cur.fetchall()
    cur.close()

    return render_template('index.html', pengunjungx = pengunjung)

@app.route('/checkin', methods = ['POST'])
# function untuk memasukkan data checkin pengunjung
def checkin():
    nama = request.form['nama_pengunjung']
    alamat = request.form['alamat_pengunjung']
    tanggal = request.form['tanggal']
    status = int(request.form['id_member'])

    cur = db.cursor()

    # cek status member
    cur.execute("SELECT id_member FROM member")
    membe = cur.fetchall()
    member = list(item[0] for item in membe)
    if status in member :
        x = 'Member'
        cur.execute("INSERT INTO pengunjung (nama, alamat, tanggal, status) VALUES (%s,%s,%s,%s)", (nama, alamat, tanggal, x))
        db.commit()
    else:
        x = 'Bukan Member'
        cur.execute("INSERT INTO pengunjung (nama, alamat, tanggal, status) VALUES (%s,%s,%s,%s)", (nama, alamat, tanggal, x))
        db.commit()
   
    return redirect(url_for('index'))

#============================================================admin====================
# function untuk masuk halaman administrator
@app.route('/admin')
def admin():
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute("SELECT * FROM pegawai")
        pegawai = cur.fetchall()
        cur.close()
        return render_template('admin.html', pegawaihtml = pegawai)
    return redirect(url_for('login'))

# function untuk masuk halaman admin-tambah (tambah pegawai)
@app.route('/admin-tambah/')
def admin_tambah():
    if 'loggedin' in session:
        return render_template('admin-tambah.html')
    return redirect(url_for('login'))
    
# function proses tambah pegawai
@app.route('/proses_admin-tambah/', methods=['POST'])
def proses_tambah():
    id_pegawai = int(request.form['id_pegawai'])
    nama = request.form['nama_pegawai']
    nik = request.form['nik_pegawai']
    alamat = request.form['alamat']
    jabatan = request.form['jabatan']

    cur = db.cursor()
    cur.execute("INSERT INTO pegawai (id_pegawai, nama, nik, alamat, jabatan) VALUES (%s, %s, %s, %s, %s)", 
                (id_pegawai, nama, nik, alamat, jabatan))
    db.commit()
    return redirect(url_for('admin'))

# function untuk masuk halaman admin-edit (edit pegawai)
@app.route('/admin-edit/<id_pegawai>', methods=['GET'])
def admin_edit(id_pegawai):
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute('SELECT * FROM pegawai WHERE id_pegawai=%s', (id_pegawai,))
        pegawai = cur.fetchall()
        cur.close()
        return render_template('admin-edit.html', pegawaihtml = pegawai)
    return redirect(url_for('login'))
    
# function untuk proses edit data pegawai
@app.route('/proses_edit/', methods=['POST'])
def proses_edit():
    id_ori = int(request.form['id_ori'])
    id = int(request.form['id'])
    nama = request.form['nama']
    nik = request.form['nik']
    alamat = request.form['alamat']
    jabatan = request.form['jabatan']
    cur = db.cursor()
    sql = "UPDATE pegawai SET id_pegawai=%s, nama=%s, nik=%s, alamat=%s, jabatan=%s WHERE id_pegawai=%s"
    value = (id, nama, nik, alamat, jabatan, id_ori)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('admin'))

# function untuk hapus pegawai
@app.route('/hapus/<id_pegawai>', methods=['GET'])
def proses_hapus(id_pegawai):
    cur = db.cursor()
    cur.execute('DELETE FROM pegawai WHERE id_pegawai=%s', (id_pegawai,))
    db.commit()
    return redirect(url_for('admin'))


# ==========================================pegawai=================================
@app.route('/pegawai')
def pegawai():
    if 'loggedin' in session:
        return render_template('pegawai.html')
    return redirect(url_for('login'))
    
#=============================================================pegawai buku===============
# function untuk masuk halaman manajemen buku
@app.route('/buku')
def buku():
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute("SELECT * FROM buku")
        buku = cur.fetchall()
        cur.close()
        return render_template('buku.html', bukuhtml = buku)
    return redirect(url_for('login'))
    
# function untuk masuk halaman buku-tambah
@app.route('/buku-tambah/')
def buku_tambah():
    if 'loggedin' in session:
        return render_template('buku-tambah.html')
    return redirect(url_for('login'))
    
# function proses tambah buku
@app.route('/proses_buku-tambah/', methods=['POST'])
def proses_bukutambah():
    id_buku = int(request.form['id_buku'])
    judul = request.form['judul']
    kategori = request.form['kategori']
    stok = int(request.form['stok'])

    cur = db.cursor()
    cur.execute("INSERT INTO buku (id_buku, judul, kategori, stok) VALUES (%s, %s, %s, %s)", 
                (id_buku, judul, kategori, stok))
    db.commit()
    return redirect(url_for('buku'))

# function untuk masuk halaman buku-edit (edit buku)
@app.route('/buku-edit/<id_buku>', methods=['GET'])
def buku_edit(id_buku):
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute('SELECT * FROM buku WHERE id_buku=%s', (id_buku,))
        buku = cur.fetchall()
        cur.close()
        return render_template('buku-edit.html', bukuhtml = buku)
    return redirect(url_for('login'))

# function untuk proses edit data buku
@app.route('/proses_buku-edit/', methods=['POST'])
def proses_bukuedit():
    id_ori = int(request.form['id_ori'])
    id_buku = int(request.form['id_buku'])
    judul = request.form['judul']
    kategori = request.form['kategori']
    stok = int(request.form['stok'])
    cur = db.cursor()
    sql = "UPDATE buku SET id_buku=%s, judul=%s, kategori=%s, stok=%s WHERE id_buku=%s"
    value = (id_buku, judul, kategori, stok, id_ori)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('buku'))

# function untuk hapus data buku
@app.route('/buku-hapus/<id_buku>', methods=['GET'])
def proses_bukuhapus(id_buku):
    cur = db.cursor()
    cur.execute('DELETE FROM buku WHERE id_buku=%s', (id_buku,))
    db.commit()
    return redirect(url_for('buku'))

#=====================================pegawai member===============================
# function untuk menampilkan halaman member
@app.route('/member')
def member():
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute("SELECT * FROM member")
        member = cur.fetchall()
        cur.close()
        return render_template('member.html', memberhtml = member)
    return redirect(url_for('login'))
    
# function untuk masuk halaman member-tambah
@app.route('/member-tambah/')
def member_tambah():
    if 'loggedin' in session:
        return render_template('member-tambah.html')
    return redirect(url_for('login'))

# function proses tambah member
@app.route('/proses_member-tambah/', methods=['POST'])
def proses_membertambah():
    id_member = int(request.form['id_member'])
    nama = request.form['nama']
    nik = request.form['nik']
    alamat = request.form['alamat']
    profesi = request.form['profesi']

    cur = db.cursor()
    cur.execute("INSERT INTO member (id_member, nama, nik, alamat, profesi) VALUES (%s, %s, %s, %s, %s)", 
                (id_member, nama, nik, alamat, profesi))
    db.commit()
    return redirect(url_for('member'))

# function untuk masuk halaman member-edit (edit member)
@app.route('/member-edit/<id_member>', methods=['GET'])
def member_edit(id_member):
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute('SELECT * FROM member WHERE id_member=%s', (id_member,))
        member = cur.fetchall()
        cur.close()
        return render_template('member-edit.html', memberhtml = member)
    return redirect(url_for('login'))

# function untuk proses edit data member
@app.route('/proses_member-edit/', methods=['POST'])
def proses_memberedit():
    id_ori = int(request.form['id_ori'])
    id_member = int(request.form['id_member'])
    nama = request.form['nama']
    nik = request.form['nik']
    alamat = request.form['alamat']
    profesi = request.form['profesi']
    cur = db.cursor()
    sql = "UPDATE member SET id_member=%s, nama=%s, nik=%s, alamat=%s, profesi=%s WHERE id_member=%s"
    value = (id_member, nama, nik, alamat, profesi, id_ori)
    cur.execute(sql, value)
    db.commit()
    return redirect(url_for('member'))

# function untuk hapus data member
@app.route('/member-hapus/<id_member>', methods=['GET'])
def proses_memberhapus(id_member):
    cur = db.cursor()
    cur.execute('DELETE FROM member WHERE id_member=%s', (id_member,))
    db.commit()
    return redirect(url_for('member'))

# =======================================pegawai pinjam====================================

# function untuk menampilkan web pinjam
@app.route('/pinjam')
def pinjam():
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute('SELECT * FROM pinjam ORDER BY id_pinjam DESC')
        pinjam = cur.fetchall()
        return render_template('pinjam.html', pinjamhtml = pinjam)
    return redirect(url_for('login'))
    
@app.route('/pinjamin', methods = ['POST'])
# function untuk memasukkan data pinjam
def pinjamin():
    member = request.form['id_member']
    buku = request.form['id_buku']
    tanggal = request.form['tanggal_pinjam']
    status = request.form['status']

    cur = db.cursor()
    if status == 'pinjam':
        cur.execute("SELECT stok FROM buku where id_buku=%s", (buku,))
        stok = cur.fetchall()
        stokint = int(stok[0][0])
        sisa = stokint - 1
        cur.execute("UPDATE buku SET stok=%s where id_buku=%s", (sisa, buku))

        # memasukkan data pinjam ke tabel pinjam
        cur = db.cursor()
        cur.execute("INSERT INTO pinjam (member, buku, tanggal_pinjam, status) VALUES (%s,%s,%s,%s)", (member, buku, tanggal, status))
        db.commit()

    elif status == 'kembalikan':
        cur.execute("SELECT stok FROM buku where id_buku=%s", (buku,))
        stok = cur.fetchall()
        stokint = int(stok[0][0])
        sisa = stokint + 1
        cur.execute("UPDATE buku SET stok=%s where id_buku=%s", (sisa, buku))
    
        # memasukkan data pinjam ke tabel pinjam
        cur.execute("INSERT INTO pinjam (member, buku, tanggal_pinjam, status) VALUES (%s,%s,%s,%s)", (member, buku, tanggal, status))
        db.commit()

    return redirect(url_for('pinjam'))

@app.route('/pinjam-view/<id_pinjam>', methods = ['GET'])
def pinjam_view(id_pinjam):
    if 'loggedin' in session:
        cur = db.cursor()
        cur.execute('SELECT * FROM pinjam WHERE id_pinjam=%s', (id_pinjam,))
        pinjam = cur.fetchall()
        tanggal_pinjam = pinjam[0][3]

        pinjam_member = pinjam[0][1]
        cur.execute('SELECT id_member, nama FROM member where id_member=%s', (pinjam_member,))
        data_member = cur.fetchall()

        pinjam_buku = pinjam[0][2]
        cur.execute('SELECT id_buku, judul, kategori FROM buku where id_buku=%s', (pinjam_buku,))
        data_buku = cur.fetchall()

        return render_template('pinjam-view.html', memberhtml = data_member, bukuhtml = data_buku, tanggalhtml = tanggal_pinjam)

    return redirect(url_for('login'))
    
@app.route('/pinjam-hapus/<id_pinjam>', methods = ['GET'])
def pinjam_hapus(id_pinjam):
    cur = db.cursor()
    cur.execute('DELETE FROM pinjam WHERE id_pinjam=%s', (id_pinjam,))
    db.commit()
    return redirect(url_for('pinjam'))

if __name__ == '__main__':
    app.run()