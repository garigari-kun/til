angular.module('app', []);

// service 'messages'
angular.module('app')
  .factory('messages', function() {
    var messages = {};

    messages.list = [];

    messages.add = function(message) {
      messages.list.push({id: messages.list.length, text: message});
    };

    return messages;

  });

// controller 'ListCtrl'
angular.module('app')
  .controller('ListCtrl', function(messages) {
    var self = this

    self.messages = messages.list;
  });

// controller 'PostCtrl'
angular.module('app')
  .controller('PostCtrl', function(messages) {
    var self = this;

    self.addMessage = function(message) {
      messages.add(message);
      self.newMessage = '';
    };
  });
