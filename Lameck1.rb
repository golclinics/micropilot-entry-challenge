require "cmath"

def getX(a, b, c)
  d = (b**2) - (4*a*c)

  x1 = (-b - CMath.sqrt(d))/(2*a)
  x2 = (-b + CMath.sqrt(d))/(2*a)

  if x1.class == Complex or x2.class == Complex
    "x1 => #{x1}, x2 => #{x2}"
  else
    [x1, x2].max
  end
end

puts(getX(5,2,1))