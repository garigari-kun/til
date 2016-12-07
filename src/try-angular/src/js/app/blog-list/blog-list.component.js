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
    templateUrl: '/templates/blog-list.html',
    controller: function($scope) {
      var blogItems = [
        {'title': 'title1','id': 1,'description': 'desc1', 'publish': '2016-12-04'},
        {'title': 'title2','id': 2,'description': 'desc2'},
        {'title': 'title3','id': 3,'description': 'desc3'},
        {'title': 'title4','id': 4,'description': 'desc4'},
      ]

      // var test = [
      //   {title: 'title1',id: 1,description: 'desc1'},
      // ]

      $scope.items = blogItems;


      $scope.title = 'Hi there';

      $scope.clicks = 0;
      $scope.someClickTest = function() {
        $scope.clicks += 1;
        $scope.title = 'Clicked ' + $scope.clicks + ' times';
      }
    }
  })
