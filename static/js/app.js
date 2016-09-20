var app = angular.module('ngoapp',['angular-loading-bar', 'ngAnimate']);

app.controller('NgoController',function($scope,$http){
    $scope.searchparam = "ngoname";
    $scope.searchvalue ="";
  $scope.searchngo = function(searchvalue) {
    $http({
  method: 'GET',
  url: '/'+$scope.searchparam+'/'+searchvalue
}).then(function successCallback(response) {
        $scope.ngos=response.data;
  }, function errorCallback(response) {

  });};



});
