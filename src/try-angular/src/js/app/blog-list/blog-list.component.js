'use strict';

// angular.module('blogList').
//   controller('BlogListController', function($scope) {
//     console.log("hello");
//     $scope.title = 'Hi there';
//     $scope.clicks = 0;
//     $scope.someClickTest = function() {
//       $scope.clicks += 1;
//       $scope.title = 'Clicked ' + $scope.clicks + ' times';
//     };
//   })

angular.module('blogList').
  component('blogList', {
    //template: '<div class = ""><h1 class = "new-class">{{ title }}</h1><button ng-click = "someClickTest()">Click me!</button></div>',
    templateUrl: '/templates/blog-list.html',
    controller: function($scope) {
      console.log("hello");
      $scope.title = 'Hi there';
      $scope.clicks = 0;
      $scope.someClickTest = function() {
        $scope.clicks += 1;
        $scope.title = 'Clicked ' + $scope.clicks + ' times';
      }
    }
  })
