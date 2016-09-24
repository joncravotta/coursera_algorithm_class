#!/usr/bin/env ruby
# by Andronik Ordian

def get_optimal_value(number_of_items, capacity, items)
  value = 0.0
  taken_items = []
  weight = capacity

  items.each do |item|
    if weight == 0
      break
    end

    a = [weight, item["weight"]].min
    value += a * item["ratio"]
    item["weight"] -= a
    weight -= a
  end



  # write your code here
  value
end

if __FILE__ == $0
  data = STDIN.read.split().map(&:to_i)
  n, capacity = data[0,2]
  values = data.values_at(*(2..2*n).step(2))
  weights = data.values_at(*(3..2*n+1).step(2))

  l = (data.length - 2) / 2
  items = []
  l.times do |i|
    hash = {}
    w = weights[i].to_f
    v = values[i].to_f
    ratio = v / w
    hash["ratio"] = ratio
    hash["weight"] = weights[i]
    hash["value"] = values[i]

    items.push(hash)
  end
  sorted = items.sort_by { |hsh| hsh["ratio"] }.reverse!
  answer = get_optimal_value(n, capacity, sorted)
  puts "#{'%.4f' % answer}"
end
