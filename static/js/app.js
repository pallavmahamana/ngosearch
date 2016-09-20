var app = angular.module('ngoapp',['angular-loading-bar', 'ngAnimate']);

app.controller('NgoController',function($scope,$http){
    $scope.searchparam = "ngoname";
    $scope.searchvalue ="";
    $scope.placeholder="Search by NGO Name";

  $scope.changeparam = function(param){
    $scope.searchparam = param;
    $('#searchtype').html(param);


    switch (param) {

      case "ngoname":$scope.placeholder="Search by Name of NGO...";
        break;
      case "regno":$scope.placeholder="Search by Registration Number...";
        break;
      case "state":$scope.placeholder="Search by State...";
        break;

      case "city":$scope.placeholder="Search by City...";
        break;
      case "sector":$scope.placeholder="Search by Sectors...";
        break;

      default:

    }


  } ;

  $scope.searchngo = function(searchvalue) {
    $http({
  method: 'GET',
  url: '/'+$scope.searchparam+'/'+searchvalue
}).then(function successCallback(response) {
        $scope.ngos=response.data;
  }, function errorCallback(response) {

  });};



});
