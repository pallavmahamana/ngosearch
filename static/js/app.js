var app = angular.module('ngoapp',[]);

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
