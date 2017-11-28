"""

Constants are mutable in Ruby


"""


module Defaults
  NETWORKS = ["192.168.1", "192.168.2"]
end


Defaults::NETWORKS.map {
  |net| net << ".100"
}

puts Defaults::NETWORKS
