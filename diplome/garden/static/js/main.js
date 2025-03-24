document.getElementById('id_master').addEventListener('change', function() {
    const masterId = this.value;
    const serviceSelect = document.getElementById('id_service');
    
    fetch(`/get-services/${masterId}/`)
        .then(response => response.json())
        .then(data => {
            serviceSelect.innerHTML = '<option value="">Select service</option>';
            data.forEach(service => {
                const option = document.createElement('option');
                option.value = service.id;
                option.textContent = service.name;
                serviceSelect.appendChild(option);
            });
        });
});