require './Lameck1'

RSpec.describe '#getX' do

  it 'returns the max if both x1 and x2 are comparable - not complex' do
    expect(getX(5,6,1)).to eq(-0.2)
  end

  it 'returns a string of both values of x1 AND x2 if either is a complex type' do
    expect(getX(5,2,1)).to eql('x1 => -1/5-0.4i, x2 => -1/5+0.4i')
  end
end