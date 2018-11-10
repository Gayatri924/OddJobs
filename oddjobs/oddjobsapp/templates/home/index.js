# install directly with gem
gem install "stream-ruby"

# or add this to your Gemfile and then run bundler
gem "stream-ruby"

require 'stream'
client = Stream::Client.new('7a7vvthtmw7d', 'dxm9bj3zdgvf84jq4m9h362svdmz8neqfryptc9jsfkhur5nz5tbvmhyt9arbrqd', :location => 'us-east')

alka = client.feed('user', 'alka')

activity_data = { :actor => 'alka', :verb => 'add', :object => 'picture:10', :foreign_id => 'picture:10', :message => 'Beautiful bird!' }
alka.add_activity(activity_data);

alka.remove_activity('picture:10', foreign_id=true)

document.getElementById("stream").innerHTML=alka
