from random import randint

while True:
    #setup
    random_number = randint(100,300)
    random_list = []

    for i in range(0, random_number):
        random_list.append(randint(10000,100000))
    print(random_number)
    print(random_list)

    slow_algo = #somefunc
    fast_algo = #somefunc
    if slow_algo != fast_algo:
        print("Problem with algos")
        print(slow_algo)
        print(fast_algo)
        break
    else
        print "OK"




# while (true) {
#   int n = rand() % 10 + 2;
#   cerr << n << "\n";
#   vector<int> a;
#   for (int i = 0; i < n; ++i) {
#     a.push_back(rand() % 100000);
#   }
#   for (int i = 0; i < n; ++i) {
#     cerr << a[i] << ' ';
#   }
#   cerr << "\n";
#   long long res1 = MaxPairwiseProduct(a);
#   long long res2 = MaxPairwiseProductFast(a);
#   if (res1 != res2) {
#     cerr << "Wrong answer: " << res1 << ' ' << res2 << "\n";
#     break;
#   }
#   else {
#     cerr << "OK\n";
#   }
# }
