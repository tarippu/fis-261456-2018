# Mamdani's Fuzzy logic based electric lamp using Python3

Logika Fuzzy disini digunakan untuk pemecahan/penarikan suatu kesimpulan pada lampu elektrik dalam memetakan suatu ruang input ke dalam ruang output. Metode Mamdani ini menghasilkan output berupa suatu nilai pada domain himpunan fuzzy yang dikategorikan ke dalam komponen linguistik.
Untuk memperoleh keputusan yang terbaik, dilakukan dengan melalui beberapa tahapan, yaitu rules, brightness, distance, power, graph

Kebutuhan input pada sistem yang akan di petakan ke dalam suatu ruang output terdiri dari distance atau jarak antara nya yang terdiri dari very far, far, not_far, close dan bighteness atau kecerahan dari lampunya seperti dark, low_brightness, medium_brightness, high_brightness. 
Input,
Distance: 50, 160, 380, 600
Brightness: 10, 500, 15, 320

Pada sistem ini proses fuzzy meliputi pengambilan nilai input sesuai dengan distance dan brightness yang diinputkan, proses fuzzifikasi dari data input, dengan menggunakan rumus fungsi keanggotaan kurva segitiga, proses logika pengambilan keputusan melalui rule-rule yang ada dan menampilkan hasil output setiap rule nya (centroid)

Output pada sistem ini berupa centroid yang sesuai dengan yang diinputkan. Kelebihan pada Metode Fuzzy Logic Mamdani adalah lebih spesifik, artinya dalam prosesnya lebih memperhatikan kondisi yang akan terjadi untuk setiap daerah fuzzynya, sehingga menghasilkan hasil keputusan yang lebih akurat.

![](https://output/output.png)


